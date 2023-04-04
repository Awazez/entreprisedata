#!/bin/sh

mkdir /tmp/some_tmp_dir                         && \
cd /tmp/some_tmp_dir                            && \
curl -L https://files.data.gouv.fr/insee-sirene/StockEtablissementHistorique_utf8.zip > file.zip && \
unzip file.zip                                  && \
rm file.zip


