import tensorflow as tf

g = tf.Graph()

with g.as_default() as g:
    tf.compat.v1.train.import_meta_graph('./checkpoints/4stack_256_mir_1k/checkpoint-15000.meta')
    file_writer = tf.summary.create_file_writer(logdir='checkpoints/file')
    tf.summary.image("my_metric",g)
    print(g)
    file_writer.flush()

#with tf.compat.v1.Session(graph=g) as sess:
