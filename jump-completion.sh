#!/bin/bash


_dothis_completions()
{
  if [ "${#COMP_WORDS[@]}" != "2" ]; then
    return
  fi

  COMPREPLY=($(compgen -W "$(cut -d ' ' -f 1 /home_ldap/lpolak/scripts/jump/host_ip.txt)" -- "${COMP_WORDS[1]}"))
  
}


complete -F _dothis_completions jump 
