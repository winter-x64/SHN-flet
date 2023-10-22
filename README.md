
![Flet](https://github.com/TH-Activities/saturday-hack-night-template/assets/90635335/4c26e8ac-2dd1-4d75-8e1a-9f7585e3b381)


# Certificate Pro
This porject is a certificate generator thats helps you to generate certificates, you can upload a certificate template and csv file with the list of participants it will automatically get the names of participants and generate the certificate for them

> Note: you can adjust the alignment of the names if needed

you can also export the certificates as a zip file or you can directly send the certificate to the participants via email address

this project helps you handle certificate distribution easier and saving more time
## Team members
1. [Akhil B Xavier](https://github.com/winter-x64)
2. [Alan Lopez ](https://github.com/oceangod2004)
2. [Angel mariya](https://github.com/angelmariy)
3. [Donavan Joseph](https://github.com/Don-ash)
## Link to product walkthrough
[link to video](Link Here)
## How it Works ?
1. Explaining the working of project
    
    firstly, the user input the template certificate and csv file with the name and email address using the **pandas library** we access the names in the and add the names to it using **pillow library** (add alignment if necessary)

    secondly, takes the name and email address from the csv file and using an email api we the send the certificate and txt to the participants

## Libraries used
- Flet
- Pillow
- pandas

## How to configure
Instructions for setting up project
- Clone repository to the local system
    ```bash
    git clone https://github.com/winter-x64/SHN-flet.git 
    ```
- venv
    ```bash
    python -m venv .venv 
    ```
- activate it
    ```bash
    .\.venv\Scripts\Activate.ps1
    ```
- install all dependencies
    ```bash
    pip install -r requirements.txt
    ```
## How to Run
- To run the project
    ```bash
    flet run main.py
    ```


