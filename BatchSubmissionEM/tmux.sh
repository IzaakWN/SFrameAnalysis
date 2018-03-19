#! /bin/bash
S="               "
tmux new session \;\
  split-window -v \;\
  send-keys 'sS; cd BatchSubmissionEM; echo "./submitIzaak.sh 1"' C-m \;\
  split-window -h \;\
  send-keys 'sS; cd BatchSubmissionEM; echo "./submitIzaak.sh 2"; echo "./submitIzaak.sh 3"' C-m \;\
  #select-pane -t 0 \;\
  #split-window -v \;\
  #send-keys 'sS; cdB' C-m \;\
  #split-window -h \;\
  #send-keys 'sS; cdB' C-m \;\
  #select-pane -t 1 \;
