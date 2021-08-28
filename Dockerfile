WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app


COPY requirements.txt .
COPY extract /usr/local/bin
COPY pextract /usr/local/bin
RUN chmod +x /usr/local/bin/extract && chmod +x /usr/local/bin/pextract
RUN sudo pip3 install -r requirements.txt 
CMD ["python3","bot.py"]
