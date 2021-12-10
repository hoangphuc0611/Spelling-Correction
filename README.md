# Introduction

Spell correction is used to detect and correct orthographic mistakes in texts. Most of the time, traditional dictionary lookup with string similarity methods is suitable for the languages that have a less complex structure such as the VietNam language.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.
```bash
$ pip install -r requirements.txt
```
## Model Used
### S2S with attention
![image](https://user-images.githubusercontent.com/53816838/145516177-11cf2a95-37f9-4769-a33f-5f2dd34c4acd.png)
### Transformer
![image](https://user-images.githubusercontent.com/53816838/145516255-450f96fd-acb2-464d-abc9-99894bd02d4f.png)

## Train model

Select the location to save the model in file translate 
Save file model to ``checkpoint-trans/...``

## RUN test
```bash
$ flask run 
```

