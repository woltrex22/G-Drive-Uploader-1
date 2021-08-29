COPY requirements.txt .
RUN sudo pip3 install -r requirements.txt 
CMD ["bash","start.sh"]
