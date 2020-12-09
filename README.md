# Data-Engineering
Exploratory Data analysis and Data pipelines for streaming data and batch processing

## use the below code to get the colab session

# Install jupyterlab and ngrok
!pip install jupyterlab pyngrok -q

# Run jupyterlab in background
!nohup jupyter lab --ip=0.0.0.0 &

# Make jupyterlab accessible via ngrok
from pyngrok import ngrok
print(ngrok.connect(8888))

## Followed by below code to get the spark environment

!apt-get install openjdk-8-jdk-headless -qq > /dev/null

# install spark (change the version number if needed)
!wget -q https://archive.apache.org/dist/spark/spark-3.0.0/spark-3.0.0-bin-hadoop3.2.tgz

# unzip the spark file to the current folder
!tar xf spark-3.0.0-bin-hadoop3.2.tgz

# set your spark folder to your system path environment. 
import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-3.0.0-bin-hadoop3.2"


# install findspark using pip
!pip install -q findspark
!pip install pyspark