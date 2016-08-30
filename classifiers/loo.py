# def separate(data, classes):
#     return [data[data[:, 0] == n, :] for n in classes]
#
# def remove_one(n, data):
#     left_out = data[n]
#     new_data = np.vstack((
#         data[:n],
#         data[(n+1):]
#     ))
#     correct_class = left_out[0]
#     classification_vector = left_out[1:]
#     return correct_class, classification_vector, new_data
#
# def leave_one_out_test_inner(n, data):
#     classes = np.unique(data[:, 0])
#
#     correct_class, classification_vector, new_data = remove_one(n, data)
#
#     separated = separate(new_data, classes)
#     models = [make_model(class_) + (class_name,)
#         for (class_, class_name) in zip(separated, classes)]
#     return classify(classification_vector, models) == correct_class
#
# def leave_one_out_test(data):
#     correct = 0
#     total = len(data)
#     for n in range(total):
#         if leave_one_out_test_inner(n, data):
#             correct += 1
#         else:
#             print("got one wrong at index %d" % n)
#     return correct, total, correct/float(total)
