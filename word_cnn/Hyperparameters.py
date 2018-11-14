# coding=UTF-8
'''
Created on 2018年7月25日

@author: zuyan
'''
class Hyperparameters:
    # training
    #batch_size = 8 # alias = N
    batch_size = 4
    lr = 0.0001 # learning rate. In paper, learning rate is adjusted to the global step.
    #logdir = 'logdir' # log directory
    logdir = "logdir_0904_part6"
    # model
    #maxlen = 8 # Maximum number of words in a sentence. alias = T.
                # Feel free to increase this if you are ambitious.
    shuffle_buffer = 4
    maxlen = 8
    min_cnt = 4 # words whose occurred less than min_cnt are encoded as <UNK>.
    hidden_units = 256 # alias = C
    num_blocks = 6 # number of encoder/decoder blocks
    num_epochs = 5
    num_epoches_test = 20
    num_heads = 8
    dropout_rate = 0.5
    sinusoid = True # If True, use sinusoid. If false, positional embedding.
    input_path = "/home/sankuai/jiangzuyan/attention/attention_tf/train_data/20180904/0904_part6"
    target_path = "/home/sankuai/jiangzuyan/attention/attention_tf/train_data/20180904/0904_part6"
    input_dict = "0904_part6_dict"
