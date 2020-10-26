class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailset = set()
        for email in emails:
            emailset.add(''.join(email.split("@")[0].split('+')[0].split('.')) + '@' + email.split("@")[1])
        return len(emailset)