import random
import preprocess
import nltk


def get_classifier():

	donnees = preprocess.get_data()
	random.shuffle(donnees)

	split = int(0.8 * len(donnees))

	donnee_train = donnees[:split]
	donne_test = donnees[split:]

	classifier = nltk.NaiveBayesClassifier.train(donnee_train)

	degre_precision = nltk.classify.util.accuracy(classifier, donne_test)
	print("Generation de Classifier")
	print('-'*70)
	print("Degrée de précision: ", degre_precision)
	return classifier
