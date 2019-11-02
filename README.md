# AZcaptcha
AZcaptcha.com team solves your CAPTCHA with high accuracy

## How to install?



### Source
```
git clone https://github.com/AZcaptcha/captcha2upload.git
cd captcha2upload
python setup.py install
```

## How to start?
[Register Here](http://AZcaptcha.com/?from=1)
And get the api key:
* Login in your account
* Go to "AZcaptcha API"
* Get "CAPTCHA Key"

# Example

## Solve Captcha
```
from captcha2upload import CaptchaUpload

captcha = CaptchaUpload(<YOURKEY>)
print captcha.solve(<PATHFILE>)
```

## Get balance
```
from captcha2upload import CaptchaUpload

captcha = CaptchaUpload(<YOURKEY>)
print captcha.getbalance()
```

## Attach the logs
```
from captcha2upload import CaptchaUpload

captcha = CaptchaUpload(<YOURKEY>, log=<YOURLOGVAR>)
print captcha.getbalance()
```

## Change Wait Time
```
from captcha2upload import CaptchaUpload

captcha = CaptchaUpload(<YOURKEY>, waittime=<YOURLOGVAR>)
print captcha.solve(<PATHFILE>)
```

