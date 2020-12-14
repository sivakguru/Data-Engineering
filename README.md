# Run Spark in Google Colab and connect the instance to Jupyter in VS Code on local machine
## use the below code to get the colab session

### Install jupyterlab and ngrok
>!pip install jupyterlab pyngrok -q

### Run jupyterlab in background
>!nohup jupyter lab --ip=0.0.0.0 &

### Make jupyterlab accessible via ngrok
>from pyngrok import ngrok
print(ngrok.connect(8888))

# Followed by below code to get the spark environment
>!apt-get install openjdk-8-jdk-headless -qq > /dev/null

### install spark (change the version number if needed)
>!wget -q https://archive.apache.org/dist/spark/spark-3.0.0/spark-3.0.0-bin-hadoop3.2.tgz

### unzip the spark file to the current folder
>!tar xf spark-3.0.0-bin-hadoop3.2.tgz

### set your spark folder to your system path environment. 
>import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-3.0.0-bin-hadoop3.2"

### install findspark using pip
>!pip install -q findspark
!pip install pyspark

### To keep the colab running, run the below code in chrome console (F12 -> console, run the code)
> function KeepClicking(){
   console.log("Clicking");
   document.querySelector("colab-toolbar-button#connect").click()
}setInterval(KeepClicking,60000)

### data sets from plotly
[Plotly datasets](https://github.com/plotly/datasets)