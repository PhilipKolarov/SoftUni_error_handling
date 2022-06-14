from email_validator_exceptions import MustContainAtSymbolError, NameTooShortError, InvalidDomainError

valid_domains = {'.org', '.net', '.bg', '.com'}
while True:
    line = input()
    if line == 'End':
        break

    email = line
    email_sections = email.split('@')

    if len(email_sections) != 2:
        raise MustContainAtSymbolError('Email must contain @')

    username = email_sections[0]
    domain = email_sections[1]

    if len(username) <= 4:
        raise NameTooShortError('Name must be longer than 4 characters')

    domain_sections = domain.split('.')
    domain_end = '.' + domain_sections[-1]

    if domain_end not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print('Email is valid')