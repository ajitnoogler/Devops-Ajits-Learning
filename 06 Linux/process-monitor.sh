#!/bin/bash

LOG_FILE="/tmp/process_monitor_$(date +%F_%H-%M-%S).log"

function log_and_print() {
    echo -e "$1" | tee -a "$LOG_FILE"
}

function top_cpu() {
    log_and_print "\n🔹 Top 5 CPU Consuming Processes:"
    ps -eo pid,ppid,cmd,%cpu,%mem --sort=-%cpu | head -n 6 | tee -a "$LOG_FILE"
}

function top_mem() {
    log_and_print "\n🔹 Top 5 Memory Consuming Processes:"
    ps -eo pid,ppid,cmd,%cpu,%mem --sort=-%mem | head -n 6 | tee -a "$LOG_FILE"
}

function zombie_check() {
    log_and_print "\n🔹 Zombie Processes:"
    ps aux | awk '$8=="Z" {print $2, $11}' | tee -a "$LOG_FILE"
}

function stopped_processes() {
    log_and_print "\n🔹 Stopped/Sleeping Processes:"
    ps aux | awk '$8 ~ /S|T/ {print $1, $2, $8, $11}' | tee -a "$LOG_FILE"
}

function port_process() {
    read -p "Enter port number to check: " PORT
    log_and_print "\n🔹 Processes using port $PORT:"
    sudo lsof -i :$PORT | tee -a "$LOG_FILE"
}

function user_process() {
    read -p "Enter username to check: " USER
    log_and_print "\n🔹 Processes run by $USER:"
    ps -u $USER -o pid,cmd,%cpu,%mem --sort=-%cpu | head -n 10 | tee -a "$LOG_FILE"
}

function process_tree() {
    log_and_print "\n🔹 Process Tree:"
    pstree -p | tee -a "$LOG_FILE"
}

function kill_high_cpu() {
    log_and_print "\n🔹 Killing processes using >80% CPU"
    ps -eo pid,%cpu --sort=-%cpu | awk '$2>80 {print $1}' | tee -a "$LOG_FILE" | xargs -r sudo kill -9
}

function save_log_summary() {
    log_and_print "\n🔹 Saving top CPU/memory snapshot into log again"
    {
        date
        echo "== TOP CPU =="
        ps -eo pid,cmd,%cpu,%mem --sort=-%cpu | head -n 6
        echo ""
        echo "== TOP MEM =="
        ps -eo pid,cmd,%cpu,%mem --sort=-%mem | head -n 6
    } >> "$LOG_FILE"
    log_and_print "✅ Log saved to $LOG_FILE"
}

### Menu Loop
while true; do
    echo -e "\n🔧 Process Monitor Menu:"
    echo "1) Top 5 CPU Processes"
    echo "2) Top 5 Memory Processes"
    echo "3) Zombie Processes"
    echo "4) Stopped/Sleeping Processes"
    echo "5) Check Process by Port"
    echo "6) Show Process Tree"
    echo "7) Show User Processes"
    echo "8) Kill Processes >80% CPU"
    echo "9) Save Summary to Log"
    echo "0) Exit"
    read -p "Choose an option: " opt

    case $opt in
        1) top_cpu ;;
        2) top_mem ;;
        3) zombie_check ;;
        4) stopped_processes ;;
        5) port_process ;;
        6) process_tree ;;
        7) user_process ;;
        8) kill_high_cpu ;;
        9) save_log_summary ;;
        0) echo -e "📝 Full log stored at: $LOG_FILE\nGoodbye!" && break ;;
        *) echo "❌ Invalid option." ;;
    esac
done
# End of script
#chmod +x process_monitor.sh
#echo "Process monitor script is ready to use. Run it with ./process_monitor.sh"
#echo "You can find the log file in /tmp/ with a timestamp." 