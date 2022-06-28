{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled3.ipynb",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AJDsIFXZHgS0",
        "outputId": "b64b9a7e-2dc7-410c-d400-66c0de7f772d"
      },
      "source": [
        "\n",
        "\n",
        "##### library import #####\n",
        "from sklearn.datasets import fetch_20newsgroups\n",
        "from sklearn.naive_bayes import MultinomialNB\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.metrics import classification_report\n",
        "\n",
        "# 밑에는 선택 알고리즘\n",
        "from sklearn.feature_extraction.text import CountVectorizer\n",
        "from sklearn.feature_extraction.text import TfidfTransformer\n",
        "import numpy as np\n",
        "\n",
        "# 분류용 샘플 데이터 불러오기\n",
        "dataset = fetch_20newsgroups()\n",
        "\n",
        "# 학습/테스트 데이터셋 분할 \n",
        "data = dataset.data\n",
        "target = dataset.target\n",
        "x_train, x_test, y_train, y_test = train_test_split(data, target,test_size=0.3, stratify=target, random_state=1)\n",
        "\n",
        "# 데이터 전처리(벡터화)\n",
        "cv = CountVectorizer() #텍스트를 단어 행렬로 변환\n",
        "tv  = TfidfTransformer() #빈도수에 따른 가중치 부여 행렬로 변환\n",
        "\n",
        "x_traincv = cv.fit_transform(x_train)\n",
        "x_testcv =cv.transform(x_test)\n",
        "\n",
        "x_traintv = tv.fit_transform(x_traincv)\n",
        "x_testtv = tv.transform(x_testcv)\n",
        "\n",
        "# 다중분류 나이브 베이즈\n",
        "model = MultinomialNB(alpha = 0.01)\n",
        "\"\"\"나이브 베이즈 객체 생성\n",
        "alpha: 결과가 0이 되는 것 방지\"\"\"\n",
        "model.fit(x_traintv, y_train) #fit: data 학습\n",
        "\n",
        "predicted = model.predict(x_testtv)\n",
        "\n",
        "\n",
        "#### do not edit here ####\n",
        "report = classification_report(y_true = y_test, y_pred = predicted)\n",
        "print('Topic 분류 결과:')\n",
        "print(report)"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Downloading 20news dataset. This may take a few minutes.\n",
            "Downloading dataset from https://ndownloader.figshare.com/files/5975967 (14 MB)\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "Topic 분류 결과:\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.92      0.92      0.92       144\n",
            "           1       0.78      0.85      0.82       175\n",
            "           2       0.86      0.80      0.83       177\n",
            "           3       0.76      0.81      0.78       177\n",
            "           4       0.83      0.88      0.85       173\n",
            "           5       0.90      0.90      0.90       178\n",
            "           6       0.82      0.74      0.78       176\n",
            "           7       0.90      0.92      0.91       178\n",
            "           8       0.95      0.94      0.94       180\n",
            "           9       0.96      0.95      0.96       179\n",
            "          10       0.95      0.96      0.96       180\n",
            "          11       0.98      0.96      0.97       179\n",
            "          12       0.86      0.84      0.85       177\n",
            "          13       0.98      0.96      0.97       178\n",
            "          14       0.96      0.96      0.96       178\n",
            "          15       0.91      0.94      0.93       180\n",
            "          16       0.94      0.98      0.96       164\n",
            "          17       0.95      0.99      0.97       169\n",
            "          18       0.93      0.90      0.92       140\n",
            "          19       0.90      0.76      0.82       113\n",
            "\n",
            "    accuracy                           0.90      3395\n",
            "   macro avg       0.90      0.90      0.90      3395\n",
            "weighted avg       0.90      0.90      0.90      3395\n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
