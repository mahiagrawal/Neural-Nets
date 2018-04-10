import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_train = X.shape[0]
  num_classes = W.shape[1]

  for i in xrange(num_train):
    scores = np.dot(X[i], W)
    scores -= np.max(scores)

    sum_exp = np.sum(np.exp(scores))
    loss += -np.log(np.exp(scores[y[i]])/sum_exp)

    for j in range(num_classes):
      dW[:, j] += (np.exp(scores[j])/sum_exp - (j == y[i]))*X[i]

  loss /= num_train
  loss += 0.5 * reg * np.sum(W * W)
  dW /= num_train
  dW += reg*W


  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  num_train = X.shape[0]

  scores = np.dot(X, W)
  scores -= np.max(scores, axis = 1, keepdims = True)

  sum_exp = np.sum(np.exp(scores), axis = 1,  keepdims = True)

  prob = np.exp(scores)/sum_exp

  loss = np.sum(-np.log(prob[np.arange(num_train), y]))
  
  ##loss = np.sum(-np.log(np.exp(scores[np.arange(num_train), y])/sum_exp))

  correct = np.zeros_like(scores)
  correct[np.arange(num_train), y] = 1

  dW = np.dot(X.T, np.exp(scores)/sum_exp - correct)

  loss /= num_train
  loss += 0.5 * reg * np.sum(W * W)
  dW /= num_train
  dW += reg*W

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

