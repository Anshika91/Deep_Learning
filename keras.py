{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMtXCUum2q2iewW/kcTT5UV",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Anshika91/Deep_Learning/blob/main/keras.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "45tr7Udr9uBq",
        "outputId": "bca3574a-b2f3-47bb-a1f4-18a838749cb3"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Model: \"sequential_3\"\n",
            "_________________________________________________________________\n",
            " Layer (type)                Output Shape              Param #   \n",
            "=================================================================\n",
            " dense_5 (Dense)             (None, 2)                 6         \n",
            "                                                                 \n",
            " dense_6 (Dense)             (None, 1)                 3         \n",
            "                                                                 \n",
            "=================================================================\n",
            "Total params: 9\n",
            "Trainable params: 9\n",
            "Non-trainable params: 0\n",
            "_________________________________________________________________\n"
          ]
        }
      ],
      "source": [
        "from keras.models import Sequential\n",
        "from keras.layers import Dense\n",
        "model=Sequential()\n",
        "model.add(Dense(2,input_dim=2,activation='relu'))\n",
        "model.add(Dense(1,activation='sigmoid'))\n",
        "model.summary()"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "-03TKE3I-ZuS"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}