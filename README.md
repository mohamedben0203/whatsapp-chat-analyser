# whatsapp-chat-analyser

Given a whatsapp conversation between two people as a txt file as an argument, this script will calculate for both users the following:

* messages sent
* words sent
* average word per message
* ratio of words sent
* ratio of messages sent
* Day where most texts have been sent
* most number of texts sent in a day

Ensure that you install the dependencies required to run this script. This can be done as follows:
``` bash
pip install -r requirements.txt
```

Or if you have python3 then

``` bash
pip3 install -r requirements.txt
```

To run the script, pass the whatsapp file as an argument. This is done as follows:

``` bash
python .\whatsappReader.py chat.txt
```
