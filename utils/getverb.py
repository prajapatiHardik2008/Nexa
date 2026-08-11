import spacy

nlp = spacy.load("en_core_web_sm")


def getVerb(text):
  doc = nlp(text)

  intent = {"action": None, "target": None, "details": []}

  # Root ya main verb find karne ke liye
  for token in doc:
    if token.pos_ in ["VERB", "AUX"] and intent["action"] is None:
      intent["action"] = token.lemma_

  # Direct object (dobj) ya compound object ko target banane ke liye
  target_words = []
  for token in doc:
    # Agar token direct object ya uska hissa hai (jaise flask, login, page)
    if token.dep_ in ["dobj", "pobj", "attr"] or (
        token.head.dep_ in ["dobj", "pobj"] and token.pos_ in ["NOUN", "ADJ"]
    ):
      # 'bro' jaise words ko skip karne ke liye
      if token.text.lower() not in ["bro", "please", "hey", "nexa"]:
        # Uske poore subtree ko collect kar lo taaki poora phrase mil jaye
        for sub in token.subtree:
          if sub.pos_ in ["NOUN", "ADJ", "PROPN"] and sub.text.lower() not in [
              "bro",
              "a",
              "an",
              "the",
          ]:
            if sub.text not in target_words:
              target_words.append(sub.text)

  if target_words:
    intent["target"] = "ج"  # ya simply join kar do
    intent["target"] = " ".join(target_words)
  else:
    # Fallback agar dobj na mile toh noun chunks use karo par 'bro' hata kar
    chunks = [
        chunk.text
        for chunk in doc.noun_chunks
        if chunk.text.lower() not in ["bro", "i", "me", "you"]
    ]
    if chunks:
      target_text = chunks[-1]  #last chunk usually main object hota hai
      words = target_text.split()
      if words and words[0].lower() in ["a", "an", "the"]:
        target_text = " ".join(words[1:])
      intent["target"] = target_text

  # Detailed tokens for verification
  for token in doc:
    intent["details"].append({
        "text": token.text,
        "pos": token.pos_,
        "dep": token.dep_,
        "lemma": token.lemma_,
    })

  return intent


# Testing
ans = getVerb("bro make a flask login page for my web site ")

print(ans['action']+" "+ans['target'])