import timeit

# py = timeit.timeit('example_py.test(10000)', setup='import example_py', number=10)
# cy = timeit.timeit('example_cy.test(10000)', setup='import example_cy', number=10)
py = timeit.timeit('email_validation.validate_email("cssrumi@gmail.com")', setup='import email_validation', number=500)
cy = timeit.timeit('email_validation_cy.validate_email("cssrumi@gmail.com")', setup='import email_validation_cy', number=500)

print('Cython is {}x times faster'.format(py/cy))
# import email_validation_cy
# print(email_validation_cy.validate_email("cssrumi@gmail.com"))

