#!/bin/sh

curl -L https://www.data.gouv.fr/fr/datasets/r/88fbb6b4-0320-443e-b739-b4376a012c32 > file.zip && \
unzip  file.zip                                  && \
rm file.zip
split -l 1000 -d StockEtablissementHistorique_utf8.csv file_
for i in $(find file_*); do mv $i "$i.csv"; done
for i in $(find . -type f -name "file_*.csv" -not -name "file_00.csv");
    do echo -e "$(head -1 file_00.csv)\n$(cat $i)" > $i;
done


