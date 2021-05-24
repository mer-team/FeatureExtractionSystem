FROM openjdk:15-alpine

ENV feature all_features
ENV inputDirectory /src/Origem/
ENV outputFile /src/Output/outputFile.csv
# ENV arg1 
# ENV arg2 nada
# ENV arg3 freq

RUN mkdir -p /src/Origem/
RUN mkdir -p /src/Output/

COPY Maininterface.jar /
COPY /src/AuxiliarFiles/DAL_ANEW.txt /src/AuxiliarFiles/DAL_ANEW.txt
COPY /src/AuxiliarFiles/Gazeteers.txt /src/AuxiliarFiles/Gazeteers.txt
COPY /src/AuxiliarFiles/gi-11788.csv /src/AuxiliarFiles/gi-11788.csv
COPY /src/AuxiliarFiles/slang.txt /src/AuxiliarFiles/slang.txt
# COPY /src/AuxiliarFiles/bidirectional-distsim-wsj-0-18.tagger /src/AuxiliarFiles/bidirectional-distsim-wsj-0-18.tagger 
# COPY /src/AuxiliarFiles/Classes-Quadrantes.txt /src/AuxiliarFiles/Classes-Quadrantes.txt

ENTRYPOINT java -jar Maininterface.jar $feature $inputDirectory $outputFile