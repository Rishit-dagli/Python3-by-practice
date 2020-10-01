# Building Better AI Apps with TensorFlow Hub

![Source: [tensorflow.org](https://www.tensorflow.org/hub)](https://cdn-images-1.medium.com/max/2400/1*G6UhfXXhlEKBvDfTghW1Qg.jpeg)

One of the best things about AI is that you have a lot of open-source content, we use them quite frequently. I will show how TensorFlow Hub makes this process a lot easier and allows you to seamlessly use pre-trained convolutions or word embeddings in your application. We will then see how we could perform Transfer Learning with TF Hub Models and also see how this can expand to other use cases.

All the code used for demos in this blog post are available at this GitHub repo-
[**Rishit-dagli/GDG-Nashik-2020**
*My session at Google Developers Group Nashik 2020. Contribute to Rishit-dagli/GDG-Nashik-2020 development by creating…*github.com](https://github.com/Rishit-dagli/GDG-Nashik-2020)

I also delivered a talk about this at GDG (Google Developers Group) Nashik, find the recorded version here-

 <iframe src="https://medium.com/media/65d1a10c9e4aa574246cf2aa7ae2f0d6" frameborder=0></iframe>

## Motivation behind TF Hub

![Source: me.me](https://cdn-images-1.medium.com/max/2000/0*Y2m1ERA62n0hxCbU)

We all use open source code, we try to make it better do some tweaks, and maybe make it work it for us. I feel this is the power of community you can share your work with people all around the world.

* Make using open source code easy

So that is the major thing TF Hub focuses on is makes using open source code, models, datasets super simple.

* Build applications faster

As a result of using pre-built content, you can develop applications faster as now you have access to work that has already been done by other people and leverage that.

* Build better applications

Not everybody has access to a high power GPU or a TPU and train models for days, you can get started off by building on open-sourced content using Transfer learning, we will see how you can leverage that. Say let us say you want to build a model that takes all reviews you receive on your product and see if they were good reviews or bad reviews. You can use word embeddings from a model trained on the Wikipedia dataset and do very well in just some time. This is a very simple example to explain it and we will see more of it later.

## What is TF Hub

* Modeling is an important part

Modeling is an important part of any Machine Learning application, you would want to invest quite some time and effort to get this right. Also note I am not saying modeling is the only important thing, in reality, there is a lot like building pipelines, serving models but we will not explore them in this blog. TF Hub helps you to do the model part better, faster, and easy.

* A way to easily discover models

![tfhub.dev](https://cdn-images-1.medium.com/max/2624/0*FzQP82cpYFGUk5Ic)

You can see a GUI and a friendly version of TensorFlow Hub at [tfhub.dev](http://tfhub.dev), you can see Hub here. You can filter models based on the type of problem you want to work for, the model format you need, and also based on the publisher. This definitely makes the model discovery process a lot easier for you.

* State of the art models

You can find a lot of well tested and state of the art models right there on TF Hub. Each of the models there on TF Hub is well documented and thoroughly tested, so you as a developer can make the best use of it. A lot of models on TF Hub even have sample Colab Notebooks to show how they work.

* Ease in using and integrating with model APIs

What is even better is that you can easily integrate it with your model APIs, so you want to have flexibility while building models, and TF Hub helps you to do so. You will then see for yourself too how well TF Hub is integrated with Keras or Core TensorFlow APIs which really makes it super easy.

* A wide array of publishers

This may not be the first thing why you would like to consider TF Hub but its good to know the wide array of publishers TF Hub, some of the major publishers are listed in the image below.

![A few publishers on TF Hub](https://cdn-images-1.medium.com/max/2022/0*K7-vZjCtIR0VnHwH)

* Without code dependencies

So a lot of times what happens is your codebases become very dependent or coupled, this can make the experimentation and iteration process a lot slower, so Hub defines artifacts for you which are not dependent on code, so you have a system which allows for faster iteration and experimentation too.

* A wide array of platforms

![Credits: [Sandeep Gupta](https://twitter.com/TheSandeepGupta)](https://cdn-images-1.medium.com/max/2000/0*IcOLp0BxN1Q7JV3U)

Another great thing about TF Hub is it does not matter if you use high-level Keras APIs or low-level APIs. You can also use it in your production-grade pipelines or systems, it integrates quite well with TensorFlow Extended too. You can also use TF.js models for web-based environments or node environments. Edge is taking off and TF Hub has covered you in that aspect too, you can use TF Lite pre-trained models to run your models directly in your mobile device and low power embedded systems. You can also discover models for Coral Edge TPUs. It is essentially just TF Lite and combining it with a powerful edge TPU.

## Understanding the idea behind using TF Hub

Let us start by talking about transfer learning, the thing which gives TF Hub it’s power. You might also know, making any model from scratch requires a good algorithm selection and architecture, lot of data, compute and of course domain expertise. That seems like quite a lot.

![The idea behind using TF Hub](https://cdn-images-1.medium.com/max/2000/1*prpbZiGBbOxCFGnEDUALSQ.png)

So what you do with TF Hub is that someone takes all this what is required to make a model from scratch makes what is called a module and then takes out some part of the model which is reusable. So in the case of text, we use word embeddings which give it a lot of power and often require quite some compute to train. In the case of images, it could be features. So you have this reusable part from a module in the TF Hub repo. With transfer learning this reusable piece could be used in your different models and it might even serve a different purpose and this is essentially how you would be using TF Hub. So when I say different purpose it could maybe be a classifier trained on a thousand labels but you just use it to predict or do a distinction between 3 classes. That’s just one example but you now maybe understand it.

**Why use Transfer Learning?**

* Generalization

Transfer Learning allows you to achieve generalization on your data, this is particularly quite helpful when you want to run your model on real-life data.

* Less data

As you have your embeddings or weights or convolutions learned pre-hand you can train high-quality models with very little data. This is very helpful when you can just not get any more data or getting more data is too costly.

* Training time

We already discussed earlier that Transfer Learning would take less time to train.

## TF Hub in Practice

* **Install TF Hub**

We will not be focussing on installing TF Hub here it is pretty straightforward, find installation steps [here](https://www.tensorflow.org/hub/installation).

* **Loading models**

You can easily load your model with this piece of code-

    MODULE_HANDLE = '[https://tfhub.dev/google/imagenet/inception_v3/classification/4](https://tfhub.dev/google/imagenet/inception_v3/classification/4)'

    module = hub.load(MODULE_URL)

You can, of course, change the MODULE_HANDLE URL for the model you need.

![](https://cdn-images-1.medium.com/max/2000/0*I-HRTDZyncMjCM4b)

So, when you call the model. load method TF Hub downloads this for you, and you will notice that it is a saved model directory and you have your model as a protobuf file which does the graph definition for you.

* Saved Model CLI

There is another great interface called the saved model CLI which I find pretty useful. This gives you a lot of useful information about your saved model like operation signatures and input-output shapes.

    !saved_model_cli show --dir [DIR] --all

Here is sample output showing the information this tool provides-

![Saved Model CLI Output](https://cdn-images-1.medium.com/max/2000/1*eOqpwck0cg893ojAaQEeTw.png)

* Inference

You can now directly perform inference with your loaded model.

    tf.nn.softmax(module([img]))[0]

But this is a bad approach as you are not generalizing your model.

## Performing Inference for Images

A lot of times it is better to use image feature vectors. They remove the final classification layer from the network and allow you to train a network on top of that allowing for greater generalization and in turn better performance on real-life data.

You could do it simply in this manner-

    model = tf.keras.Sequential([

      hub.KerasLayer(MODULE_HANDLE,

                     input_shape=IMG_SIZE + (3,),

                     output_shape=[FV_size],

                     trainable=True),

      tf.keras.layers.Dense(NUM_CLASSES,

                            activation='softmax')])

So you can see I now use hub.KerasLayer to create my model as a Keras layer and I also set trainable to be True as I want to perform transfer learning.

So we can then have our model add a Dense layer after it so you are taking the model adding your own layers and then retraining it with the data you have, of course, you could have multiple layers or even convolutional layers on top of this. And then you could fit it like any other Keras model after compiling it. The fitting and compiling process remains the same which shows us the level of integration of TF Hub.

## Working with text-based models

![](https://cdn-images-1.medium.com/max/2000/0*m3O4KLOx6ymQw1Q0)

One of the major problems we need to address when converting text to numbers is you need to do it in a way you preserve the meaning or semantic of text. We often use what is called word embeddings to do so. So as you can see above word vectors are as the names suggest vectors and semantically similar words have a similar direction of vectors. The dimensions of the size of the vector are also called embedding dimensions. Most part of the training is about learning these embeddings.

I would load embedding something like this-

    embedding = "URL"

    hub_layer = hub.KerasLayer(embedding,

                               input_shape=[], 
                               dtype=tf.string,

                               trainable=True)

The loading part is where things get a bit different, so you would do something like this to specify that you are loading embeddings and then you are all ready to use this in your neural net, in the same manner, we did earlier. So there was not much difference in practice but it is good to know how you could handle word embeddings

**Another thing to consider**

There is in fact another added feature with this. Let’s say I am using an embedding layer that returns me 20-dimensional embedding vectors. This means if you pass in a single word it returns you a 1 by 20 array.

![Single-word embeddings](https://cdn-images-1.medium.com/max/2000/1*v0oSxkvd1GnCu6rGuEEpQA.png)

Let’s say I pass two sentences, I want you to look at the output shape its 2 by 20 the 2 is of course because I passed a list with two items but why do I have a 20. 20-dimensional output vector should be there for each word so why do I have a 20-dimensional vector for a complete sentence. It intelligently converts these word embeddings to sentence embeddings for you and you no longer have to worry about keeping the shape constant or things like that.

![Embeddings for two sentences](https://cdn-images-1.medium.com/max/2000/1*MW5f4XauJva1iaOWmmxt7A.png)

## Trying out some examples!

I strongly recommend you to try out these examples for yourself, they can be run in Colab itself. Find them at the GitHub repo for this post-
[**Rishit-dagli/GDG-Nashik-2020**
*My session at Google Developers Group Nashik 2020. Contribute to Rishit-dagli/GDG-Nashik-2020 development by creating…*github.com](https://github.com/Rishit-dagli/GDG-Nashik-2020)

 1. Neural Style Transfer

A neural style transfer algorithm would ideally require quite some amount of compute and time, we can use TensorFlow Hub to do this easily. We will start by defining some helper functions to convert images to tensors and vice-versa.

 <iframe src="https://medium.com/media/a1112c0bf8951258fd4964ffe5f0c120" frameborder=0></iframe>

You can then convert the images to tensors, create an arbitrary [image stylization model](https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2) model and we can start building images right away!

    hub_module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

    combined_result = hub_module(tf.constant(content_image_tensor[0]), tf.constant(style_image_tensor[1]))[0]

    tensor_to_image(combined_result)

With this, you can now create an image like this(images in GitHub repo)-

![The output ofNeural Style Transfer](https://cdn-images-1.medium.com/max/2000/1*Oai_WW1eJA5PZK4OGUgqpQ.png)

2. Text Classification

We will now see how we could make a model that uses Transfer Learning. We will try our hands on the IMDB dataset to predict if a comment is positive or negative. We can use the gnews-swivel embedding which were trained on 130 GB Google News data.

So, we can have our model loaded simply like this-

    embedding = "https://tfhub.dev/google/tf2-preview/gnews-swivel-20dim/1"
    
    hub_layer = hub.KerasLayer(embedding, input_shape=[], dtype=tf.string, trainable=**True**)

We can then build a model on top of that-

    model = tf.keras.Sequential([
            hub_layer,
            tf.keras.layers.Dense(16, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')])

And then you could train your model like any other Keras model

## About Me

Hi everyone I am Rishit Dagli

[Twitter](https://twitter.com/rishit_dagli)

[Website](https://rishit.tech/)

If you want to ask me some questions, report any mistake, suggest improvements, give feedback you are free to do so by emailing me at —

* [rishit.dagli@gmail.com](mailto:rishit.dagli@gmail.com)

* [hello@rishit.tech](mailto:hello@rishit.tech)
