# VertexIA
Cloud Function

El siguiente script en Python es una API para Google Cloud Functions.
Éste hace uso de un modelo en Vertex AI sobre el modelo de estraccion de entidades previamente entrenado.

En el siguiente apartado, proporcionamos los siguientes datos de nuesto modelo:

        projectr: str = ""
        endpoint_idr: str = ""
        locationr: str = ""
        api_endpointr: str = ""
        
Despues, dentro de nuestra función predict(), se imprime el json predictions, que es el resultado que nos da nuestro modelo, despues de haberle mandado el texto.
Por consiguiente, la funcion sample_analyze_sentiment() hace un analisis de nuestro texto para saber cual es su sentimiento, regresando un Score de entre 1 y -1, donde uno es POSITIVO y menos uno NEGATIVO.
En la parte siguiente parte:

        if request.method == 'POST':
          result={}
          predicciones={}
          predicciones['Predicciones']=[]
          request_json = request.get_json()
          comments_in = request_json['comments']
          for x in range(len(comments_in)):
              result = predic(comments_in[x][0],comments_in[x][1],x,result,predicciones)
              print (result);
          return (json.dumps({"end":"fin"}), 200, {'Content-Type': 'application/json'})
          
Al recibir un metodo POST, recibe un json, de donde se extrae la informacion, aqui se procesa y se envia a las funciones posterioes antes mensionadas.

Nota: Para la utilización de este script, es necesario tener una facturacion con google cloud platform. despues instalar las dependencias de google en nuestro dispositivo con las credenciales para poder hacer uso de manera local. Para hacer uso de este script es necesario tener una facturacion en google cloud platform. mas informacion en https://cloud.google.com/
