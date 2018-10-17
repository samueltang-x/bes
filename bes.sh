#!/bin/bash

# Enable alias inside shell
shopt -s expand_aliases

fullFilePath=$(realpath $0)
baseDir=$(dirname "${fullFilePath}")

pidFile="${baseDir}/pid.lock"

logger="${baseDir}/lib/logger.sh"
logFile="${baseDir}/log/bes.log"

if [[ -f "${logger}" ]]
then
  source "${logger}"

  alias ERROR='logger ERROR'
  alias WARNING='logger WARNING'
  alias INFO='logger INFO'
  alias DEBUG='logger DEBUG'

  __logging_level='INFO'
  #__logging_level='DEBUG'
  # Redirect output to std out, instead of log file
  __redirect_to_standard_out=TRUE
  # Set time format like: 2016-10-19 17:57:00.372
  __logger_time_format='%F %T.%3N'

  logger DEBUG "logger module loaded."

else
  alias ERROR='echo'
  alias WARNING='echo'
  alias INFO='echo'
  alias DEBUG='echo'
fi

function usage() {
  echo "
Usage:
  ${BASH_SOURCE[0]} {status|start|stop|restart|help} [https|http]

  options:

  examples:
    ./bes.sh status
    ./bes.sh start
    ./bes.sh stop
    ./bes.sh start http
"
}

function getPpidByPid() {
  local errorMsg="Function ${FUNCNAME} requires one PID argument."
  local pid=${1:?"${errorMsg}"}
  
  local ppid=$(ps -o pid --no-headers --ppid ${pid})
  echo -ne ${ppid}
}

function checkServerStatus() {
  local NORMAL=$(tput sgr0)
  local GREEN=$(tput setaf 2)
  local RED=$(tput setaf 1)

  local pid=$(cat ${pidFile})
  DEBUG "Read from PID file: ${pid}"

  if [[ -z $pid ]]
  then
    INFO "Server is ${RED}Down${NORMAL}."
    exit 0
  fi

  #local ouput=$(ps ${pid})
  ps ${pid} > /dev/null
  if [[ $? -eq '0' ]]
  then
    INFO "Server is ${GREEN}running${NORMAL} with PID: ${pid}."
  else
    INFO "Server is ${RED}Down${NORMAL}."
    DEBUG "Be going to remove PID ${pid} from locking file."
    > $pidFile
  fi
}

function startServer() {
  case "${httpSheme}" in
    https)
      INFO "Be going to start server in ${httpSheme} mode."
      server=${baseDir}/run_https.py
      ;;
    http)
      server=${baseDir}/run.py
      INFO "Be going to start server in ${httpSheme} mode."
      ;;
    *)
      ERROR "Invalid HTTP model provided, mush be https or http."
      ERROR "Model: $httpSheme"
      exit 1
      ;;
  esac
  
  ${server} >> ${logFile} 2>&1 &
  local callerPid=$!
  sleep 1
  local pid=$(getPpidByPid ${callerPid})
  DEBUG "Startup info: PPID - ${callerPid}, PID - ${pid}"

  if [[ -z $pid ]]
  then
    ERROR "Oops, starting server failed!"
  else
    INFO "Server is staring with PID: $pid"
    echo -ne ${pid} > ${pidFile}
  fi
}


function stopServer () {
  local pid=$(cat ${pidFile})
  if [[ -z $pid ]]
  then
    WARNING "No PID found from PID file, please check if server is running."
    exit 1
  fi

  kill $pid
  sleep 1
  
  ps $pid > /dev/null
  if [[ $? -eq '1' ]]
  then
    INFO "Server with PID ${pid} is stopped successfully."
    > ${pidFile}
  else
    WARNING "Something unexpected happens, please check manually."
  fi
}


action=${1:-help}
httpSheme=${2:-https}

case "${action}" in
  help)
    usage
    exit 0
    ;;
  status)
    DEBUG 'check status'
    checkServerStatus
    #checkStatus
    ;;
  stop)
    stopServer
    ;;
  start)
    startServer
    ;;
  test_getPpidByPid)
    ppid=$(getPpidByPid 24538)
    DEBUG "PPID is: ${ppid}"
    ;;
  *)
    ERROR "The first argument is invalid: ${action}"
    exit 1
    ;;
esac
