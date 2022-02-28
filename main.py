from google.cloud import aiplatform
from google.cloud.aiplatform.gapic.schema import predict
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value
from google.cloud import language_v1
import six
import json

def prediction_coments(request):

    def clean(comentario,characters):
        for x in range(len(characters)):
            comentario = comentario.replace(characters[x],"")
        for x in range(len(characters)):
            comentario = comentario.replace("á","a")
        for x in range(len(characters)):
            comentario = comentario.replace("é","e")
        for x in range(len(characters)):
            comentario = comentario.replace("í","i")
        for x in range(len(characters)):
            comentario = comentario.replace("ó","o")
        for x in range(len(characters)):
            comentario = comentario.replace("ú","u")
        return comentario

    def sample_analyze_sentiment(content):
        client = language_v1.LanguageServiceClient()
        if isinstance(content, six.binary_type):
            content = content.decode("utf-8")
        type_ = language_v1.Document.Type.PLAIN_TEXT
        document = {"type_": type_, "content": content}
        response = client.analyze_sentiment(request={"document": document})
        sentiment = response.document_sentiment
        return (sentiment.score)

    def predic(kyprim,mensaje,n,predict_full_json,predicciones):
        projectr: str = ""
        endpoint_idr: str = ""
        locationr: str = ""
        api_endpointr: str = ""

        client_options = {"api_endpoint": api_endpointr}
        client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)
        instance = predict.instance.TextClassificationPredictionInstance(
            content=mensaje,
        ).to_value()
        instances = [instance]
        parameters_dict = {}
        parameters = json_format.ParseDict(parameters_dict, Value())
        endpoint = client.endpoint_path(
            project=projectr, location=locationr, endpoint=endpoint_idr
        )
        response = client.predict(
            endpoint=endpoint, instances=instances, parameters=parameters
        )

        
        predictions = response.predictions

        #impresion de las predicciones segun el modelo VertexAI
        print (predictions)
        #se llama a function clean para limpiar un poco el comentario
        #se hace al llamdo de analisis de comentarios
        #impresion de el score del sentimiento respecto al comentario mandado
        print (sample_analyze_sentiment(clean("comentario a procesar sentimiento","\n")))
        return ("terminado")

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
    
    elif request.method == 'GET':
        data_get = {"comments":[["ID de cometnario","Comentario a procesar"],
                                ["300","Me siento Feliz"],
                                ["...","..."]]}
        return (json.dumps(data_get), 200, {'Content-Type': 'application/json'})
