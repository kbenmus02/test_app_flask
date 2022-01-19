# Lancer le serveur : flask run
# Tutoriel : https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask
# Images : C:\Users\René\Documents\Rene\IA\IA297\Jupyter\420-A62-BB_ProjetSynthese\A62-EquipeCV\cell_images\Parasitized
import os.path
import os
import imghdr
import glob

import pandas as pd
import numpy as np
import cv2
import fnmatch #Permet de filtrer les noms de fichier selon l'extention.
import utils

from flask import Flask, \
    abort, \
    redirect, \
    render_template, \
    request, \
    send_from_directory, \
    url_for

from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"]=50 * 1024 #50 Ko
app.config["UPLOAD_EXTENSIONS"] = [".png"]
app.config["UPLOAD_PATH"] = "uploaded_img" # Le répertoire doit exister avant d'être utilisé.

PATH_ROOT = ".."
PATH_NOTEBOOK = PATH_ROOT + "/notebook"
PATH_MODEL = PATH_ROOT + "/model"
MODEL_FILE_NAME = "model_rf_rm_2021-01-16_14h28.pklz"
IMG_SIZE = 64
IMG_IN_COLOR = 1

@app.route("/")
def index():
    
    #img_file_name_list = fnmatch.filter(os.listdir(app.config['UPLOAD_PATH']), "*.png") #Liste des images dans le répertoire UPLOAD_PATH.
    #print("### Index(), av predict()")
    #prediction_table_row_list = predict()
    #print("###", prediction_table_row_list)
    #print("### Index(), ap predict()")
    return render_template('index.html')#, file_name_list=img_file_name_list, table_row_list = prediction_table_row_list)

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    app.run(debug=False, host="0.0.0.0", port = port)