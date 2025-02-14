from sgnlp.models.lsr import LsrModel, LsrConfig, LsrPreprocessor, LsrPostprocessor
from transformers import cached_path

# Download files from azure blob storage
rel2id_path = cached_path('https://sgnlp.blob.core.windows.net/models/lsr/rel2id.json')
word2id_path = cached_path('https://sgnlp.blob.core.windows.net/models/lsr/word2id.json')
ner2id_path = cached_path('https://sgnlp.blob.core.windows.net/models/lsr/ner2id.json')
rel_info_path = cached_path('https://sgnlp.blob.core.windows.net/models/lsr/rel_info.json')

PRED_THRESHOLD = 0.3
preprocessor = LsrPreprocessor(rel2id_path=rel2id_path, word2id_path=word2id_path, ner2id_path=ner2id_path)
postprocessor = LsrPostprocessor.from_file_paths(rel2id_path=rel2id_path, rel_info_path=rel_info_path,
                                                 pred_threshold=PRED_THRESHOLD)

# Load model
config = LsrConfig.from_pretrained('https://sgnlp.blob.core.windows.net/models/lsr/v2/config.json')
model = LsrModel.from_pretrained('https://sgnlp.blob.core.windows.net/models/lsr/v2/pytorch_model.bin', config=config)
model.eval()

# DocRED-like instance
instance = {
    "vertexSet": [[{"name": "Lark Force", "pos": [0, 2], "sent_id": 0, "type": "ORG"},
                   {"sent_id": 3, "type": "ORG", "pos": [2, 4], "name": "Lark Force"},
                   {"name": "Lark Force", "pos": [3, 5], "sent_id": 4, "type": "ORG"}],
                  [{"name": "Australian Army", "pos": [4, 6], "sent_id": 0, "type": "ORG"}],
                  [{"pos": [9, 11], "type": "TIME", "sent_id": 0, "name": "March 1941"}],
                  [{"name": "World War II", "pos": [12, 15], "sent_id": 0, "type": "MISC"}],
                  [{"name": "New Britain", "pos": [18, 20], "sent_id": 0, "type": "LOC"}],
                  [{"name": "New Ireland", "pos": [21, 23], "sent_id": 0, "type": "LOC"}],
                  [{"name": "John Scanlan", "pos": [6, 8], "sent_id": 1, "type": "PER"}],
                  [{"name": "Australia", "pos": [13, 14], "sent_id": 1, "type": "LOC"}],
                  [{"name": "Rabaul", "pos": [17, 18], "sent_id": 1, "type": "LOC"},
                   {"name": "Rabaul", "pos": [12, 13], "sent_id": 3, "type": "LOC"}],
                  [{"name": "Kavieng", "pos": [19, 20], "sent_id": 1, "type": "LOC"},
                   {"name": "Kavieng", "pos": [14, 15], "sent_id": 3, "type": "LOC"}],
                  [{"pos": [22, 24], "type": "MISC", "sent_id": 1, "name": "SS Katoomba"}],
                  [{"pos": [25, 27], "type": "MISC", "sent_id": 1, "name": "MV Neptuna"}],
                  [{"name": "HMAT Zealandia", "pos": [28, 30], "sent_id": 1, "type": "MISC"}],
                  [{"name": "Imperial Japanese Army", "pos": [8, 11], "sent_id": 3, "type": "ORG"}],
                  [{"pos": [18, 20], "type": "TIME", "sent_id": 3, "name": "January 1942"}],
                  [{"name": "Japan", "pos": [8, 9], "sent_id": 4, "type": "LOC"}],
                  [{"pos": [12, 13], "type": "MISC", "sent_id": 4, "name": "NCOs"}],
                  [{"name": "USS Sturgeon", "pos": [20, 22], "sent_id": 4, "type": "MISC"}],
                  [{"sent_id": 4, "type": "MISC", "pos": [27, 29], "name": "Montevideo Maru"}],
                  [{"name": "Japanese", "pos": [5, 6], "sent_id": 5, "type": "LOC"}],
                  [{"pos": [15, 16], "type": "NUM", "sent_id": 5, "name": "1,050"}],
                  [{"pos": [17, 18], "type": "NUM", "sent_id": 5, "name": "1,053"}]],
    "labels": [
        {"r": "P607", "h": 1, "t": 3, "evidence": [0]},
        {"r": "P17", "h": 1, "t": 7, "evidence": [0, 1]},
        {"r": "P241", "h": 6, "t": 1, "evidence": [0, 1]},
        {"r": "P607", "h": 6, "t": 3, "evidence": [0, 1]},
        {"r": "P27", "h": 6, "t": 7, "evidence": [0, 1]},
        {"r": "P1344", "h": 7, "t": 3, "evidence": [0, 1]},
        {"r": "P607", "h": 13, "t": 3, "evidence": [0, 3]},
        {"r": "P17", "h": 13, "t": 15, "evidence": [3, 4, 5]},
        {"r": "P17", "h": 13, "t": 19, "evidence": [3, 4, 5]},
        {"r": "P1344", "h": 15, "t": 3, "evidence": [0, 3, 4, 5]},
        {"r": "P172", "h": 15, "t": 19, "evidence": [4, 5]},
        {"r": "P607", "h": 17, "t": 3, "evidence": [0, 4]},
        {"r": "P17", "h": 11, "t": 7, "evidence": [1]},
        {"r": "P17", "h": 12, "t": 7, "evidence": [0, 1]},
        {"r": "P137", "h": 0, "t": 1, "evidence": [0, 1]},
        {"r": "P571", "h": 0, "t": 2, "evidence": [0]},
        {"r": "P607", "h": 0, "t": 3, "evidence": [0]},
        {"r": "P17", "h": 0, "t": 7, "evidence": [0, 1]}],
    "title": "Lark Force",
    "sents": [
        ["Lark", "Force", "was", "an", "Australian", "Army", "formation", "established", "in", "March", "1941",
         "during", "World", "War", "II", "for", "service", "in", "New", "Britain", "and", "New", "Ireland", "."],
        ["Under", "the", "command", "of", "Lieutenant", "Colonel", "John", "Scanlan", ",", "it", "was", "raised", "in",
         "Australia", "and", "deployed", "to", "Rabaul", "and", "Kavieng", ",", "aboard", "SS", "Katoomba", ",", "MV",
         "Neptuna", "and", "HMAT", "Zealandia", ",", "to", "defend", "their", "strategically", "important", "harbours",
         "and", "airfields", "."],
        ["The", "objective", "of", "the", "force", ",", "was", "to", "maintain", "a", "forward", "air", "observation",
         "line", "as", "long", "as", "possible", "and", "to", "make", "the", "enemy", "fight", "for", "this", "line",
         "rather", "than", "abandon", "it", "at", "the", "first", "threat", "as", "the", "force", "was", "considered",
         "too", "small", "to", "withstand", "any", "invasion", "."],
        ["Most", "of", "Lark", "Force", "was", "captured", "by", "the", "Imperial", "Japanese", "Army", "after",
         "Rabaul", "and", "Kavieng", "were", "captured", "in", "January", "1942", "."],
        ["The", "officers", "of", "Lark", "Force", "were", "transported", "to", "Japan", ",", "however", "the", "NCOs",
         "and", "men", "were", "unfortunately", "torpedoed", "by", "the", "USS", "Sturgeon", "while", "being",
         "transported", "aboard", "the", "Montevideo", "Maru", "."],
        ["Only", "a", "handful", "of", "the", "Japanese", "crew", "were", "rescued", ",", "with", "none", "of", "the",
         "between", "1,050", "and", "1,053", "prisoners", "aboard", "surviving", "as", "they", "were", "still",
         "locked", "below", "deck", "."]
    ]
}

tensor_doc = preprocessor([instance])
output = model(**tensor_doc)

result = postprocessor(output.prediction, [instance])
