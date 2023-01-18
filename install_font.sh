#!/bin/bash

directorio_destino='/usr/share/fonts'
cantidad_argumentos=$#
directorio_final=$1$2
num=2

if [[ $cantidad_argumentos -eq $num ]];then
  if [ -d $1 ];then
    directorio_archivo_zip=$1
    file=$2
    sudo mv $directorio_final $directorio_destino
    cd $directorio_destino
    nombre_carpeta=${file%.*} 
    sudo mkdir $nombre_carpeta
    sudo mv $file $nombre_carpeta
    cd $nombre_carpeta
    echo "unzip $file"
    sudo unzip $file 
    sudo fc-cache -f -v
  else
    echo "Directorio invalido"
    echo $directorio_archivo_zip
  fi
else
  echo 'Algo salio mal'
fi





