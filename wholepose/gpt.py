# -*- coding: iso-8859-9 -*-
import sys

import openai

list_of_words_str =sys.argv[1]


openai.api_key = "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"

prompt = f"{list_of_words_str} c�mlesi T�rk�e kurallar�na uygun de�il. Bu c�mleyi T�rk�e kurallar�na uygun bir hale getir. Bu c�mle bir uygulamada kullan�laca��ndan �t�r� a��klama yapma sadece ��kt�y� yaz. Sadece c�mleyi yaz."

try:
    result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=1,
    )
    if len(result) > 50:
        print(list_of_words_str)
    else:
        out = result['choices'][0]['message']['content']
        out = out.replace('"', '')
        # out = out[0:-1]
        # out = out[1:]
        print(out)
except:
    print(list_of_words_str)
