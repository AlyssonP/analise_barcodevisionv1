import os
from ast import literal_eval

def processarArquivoMetrica(path_arquivo, resolucao):
    dados = []
    with open(path_arquivo, "r") as arquivo:
        for l in arquivo:
            if('FRAME' in l):
                dado_process = {}
                detectado = False
                lido = False
                dado_dict = literal_eval(l)
                dado_process["frame"] = dado_dict["FRAME"]
                dado_process["resolucao"] = resolucao
                dado_process["time_process_ms"] = dado_dict["TIME_PROCESS_MS"]
                if("BARCODE" in dado_dict):
                    detectado = True
                    if(dado_dict["BARCODE"] != None):
                        lido = True
                dado_process["detected"] = detectado
                dado_process["read"] = lido
                dados.append(dado_process)
    return dados

def processarPastaMetricas(pasta_metricas):
    dados_metrica = []
    for arquivo in os.listdir(pasta_metricas):
        if os.path.isfile(os.path.join(pasta_metricas, arquivo)):
            resolucao = arquivo.split("_")[0]
            caminho = pasta_metricas+arquivo
            print("Processando dados da resolução",resolucao)
            dados_metrica += processarArquivoMetrica(path_arquivo=caminho, resolucao=resolucao)
    return dados_metrica

def transformMetricaCSV(dados, nomeArquivo):
    with open(f"{nomeArquivo}.csv", "w") as f:
        f.write(",".join(dados[0].keys()))
        f.write("\n")
        for row in dados:
            f.write(",".join(str(x) for x in row.values()))
            f.write("\n")


print("Processando dados Zbar")
path = "dados_metricas/zbar/"
dados = processarPastaMetricas(pasta_metricas=path)
transformMetricaCSV(dados=dados, nomeArquivo="zbar")
print()

print("Processando dados Zbar Rotate Multithread")
path = "dados_metricas/zbar_rotate_multithread/"
dados = processarPastaMetricas(pasta_metricas=path)
transformMetricaCSV(dados=dados, nomeArquivo="zbar_rotate_multithread")
print()

print("Processando dados Yolo ROI 15 Zbar Multithread")
path = "dados_metricas/yolo_roi_15_zbar_multithread/"
dados = processarPastaMetricas(pasta_metricas=path)
transformMetricaCSV(dados=dados, nomeArquivo="yolo_roi_15_zbar_multithread")
print()

print("Processando dados Yolo ROI 25 Zbar Multithread")
path = "dados_metricas/yolo_roi_25_zbar_multithread/"
dados = processarPastaMetricas(pasta_metricas=path)
transformMetricaCSV(dados=dados, nomeArquivo="yolo_roi_25_zbar_multithread")
print()

print("Processando dados Yolo ROI 35 Zbar Multithread")
path = "dados_metricas/yolo_roi_35_zbar_multithread/"
dados = processarPastaMetricas(pasta_metricas=path)
transformMetricaCSV(dados=dados, nomeArquivo="yolo_roi_35_zbar_multithread")
print()

print("Processando dados Yolo Detecta e Zbar ler em Multithread")
path = "dados_metricas/yolo_detecta_zbar_ler_multithread/"
dados = processarPastaMetricas(pasta_metricas=path)
transformMetricaCSV(dados=dados, nomeArquivo="yolo_detecta_zbar_ler_multithread")
print()

print("Processamento realizado com sucesso!")