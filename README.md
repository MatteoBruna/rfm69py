#Python script to operate rfm69 ardio using Raspberry Pi

Code based on:
https://github.com/etrombly/RFM69

Communications to nodes based on:
https://github.com/LowPowerLab/RFM69

# Hardware setup

Attach the RFM69 as follows: (to check)

| RFM pin | Pi pin  
| ------- |-------
| 3v3     | 17  
| DIO0    | 18 (GPIO24)  
| MOSI    | 19  
| MISO    | 21  
| CLK     | 23  
| NSS     | 24  
| Ground  | 25  
| RESET   | 28


# Prerequisites

RPi.GPIO and spidev

If you are using newer firmware you'll need to get a newer spidev, the old one is no longer working:

```bash
git clone https://github.com/Gadgetoid/py-spidev
cd py-spidev
sudo make install
```