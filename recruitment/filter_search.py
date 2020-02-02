import numpy as np
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import pandas as pd
l = [['Technology', 'Data', 'Forecasting', 'Digital', 'Python', 'Skills'], ['Technology', 'Amazon', 'Tamil', 'Skills', 'Survey'], ['Collaboration', 'Technology', 'Cisco', 'Communication', 'Video', 'Productivity', 'Electronics', 'Apple'], ['Collaboration', 'Console', 'Technology', 'Alchemy', 'Maps', 'Plants', 'Unreal', 'English', 'Ownership', 'Live', 'Software', 'Unity', 'Games', 'Art', 'ZBrush', 'Anatomy', 'Displacement', 'Rigging'], ['Web', 'Technology', 'Software', 'Design'], ['Hiring', 'Health', 'Performing', 'LTD'], [], ['Packaging', 'Internet', 'Customer', 'Salary', 'Commission', 'Options', 'SME', 'Management', 'APAC', 'Telco'], ['Water', 'Health', 'Surface', 'Liaison', 'Coaching', 'Mentoring', 'Design', 'Building', 'EPANET', 'Performing'], ['Git', 'MySQL', 'PostgreSQL', 'Database', 'Java', 'Nginx', 'STS', 'Confluence', 'Spring', 'Enterprise', 'Framework'], ['Intelligence', 'Sequoia', 'Technology', 'Google', 'Data', 'IT', 'Kibana', 'Customer', 'Reporting', 'SQL', 'Capital', 'CRM', 'SaaS', 'Advanced', 'Analytics'], ['SAP'], ['Git', 'TestNG', 'Technology', 'Software', 'Integration', 'IP', 'SQL', 'Agile', 'Selenium', 'Skills'], ['Manufacturing', 'Engineers', 'Membership', 'EPC', 'Online', 'Electronics', 'Codes', 'Project', 'Skills'], ['Technology', 'Excel', 'Customer', 'WIP', 'Handover', 'MEP', 'Project'], ['Git', 'Technology', 'MySQL', 'PHP', 'Python', 'SQL'], ['RabbitMQ', 'AWS', 'Cassandra', 'Software', 'Unix', 'Spring', 'Ansible', 'Puppet', 'Python', 'Oracle', 'Kafka'], ['Cloud', 'Technology', 'Communications', 'Recruiting', 'NSX', 'Design', 'IP', 'Firewall', 'Alto', 'Security', 'Internet', 'Skills'], ['Facilitation', 'Project', 'IT'], ['Technology', 'Hadoop', 'ITIL', 'Application', 'Unix', 'Finance', 'Oracle', 'Cloudera'], ['Cloud', 'Technology', 'Apache', 'Data', 'Azure', 'Hadoop', 'Kubernetes', 'Microsoft', 'Enterprise', 'Building', 'Contribute'], ['Data', 'ETL', 'Integration', 'Insurance', 'SQL', 'Modeling', 'SAP'], ['Technology', 'MySQL', 'Java', 'Guidewire', '.NET', 'SQL'], ['Cloud', 'Technology', 'Azure', 'IT', 'AWS', 'Application', 'Enterprise', 'Design', 'DevOps', 'IBM', 'Blockchain'], ['Web', 'Retail', 'Testing', 'Technology', 'Recruiting', 'IT', 'API', 'SOA', 'Infrastructure', 'CTC', 'Salary', 'Software', 'Enterprise', 'Apps', 'Async', 'Design', 'Recruiter', 'REST', 'Internet', 'Skills']]
s=['Membership',
 'Oracle',
 'Hadoop',
 'Contribute',
 'Plants',
 'DevOps',
 'CRM',
 'Apps',
 'SaaS',
 'AWS',
 'Cloud',
 'Integration',
 'Maps',
 'ETL',
 'ITIL',
 'Spring',
 'Analytics',
 'NSX',
 'Python',
 'Recruiter',
 'Apple',
 'Recruiting',
 'Telco',
 'Electronics',
 'Amazon',
 'Manufacturing',
 'Salary',
 'API',
 'Packaging',
 'Games',
 'Hiring',
 'Art',
 'Live',
 'Health',
 'Database',
 'Unity',
 'PHP',
 'Apache',
 'Alchemy',
 'Kibana',
 'Blockchain',
 'Performing',
 'Ansible',
 'Kafka',
 'Building',
 'SOA',
 'MEP',
 'Technology',
 'Survey',
 'Options',
 'Firewall',
 'Finance',
 'PostgreSQL',
 'EPC',
 'Communication',
 'MySQL',
 'Sequoia',
 'Skills',
 'Productivity',
 'IBM',
 'Retail',
 'Cloudera',
 'Cassandra',
 'Water',
 'Online',
 'LTD',
 'Security',
 'Anatomy',
 'ZBrush',
 'Guidewire',
 'Insurance',
 'Handover',
 'Kubernetes',
 'CTC',
 'RabbitMQ',
 'Microsoft',
 'IT',
 'SQL',
 'Application',
 'Software',
 'Excel',
 'Nginx',
 'Collaboration',
 'Alto',
 'Testing',
 'Video',
 'Google',
 '.NET',
 'Data',
 'STS',
 'Management',
 'Async',
 'Web',
 'Agile',
 'Advanced',
 'Internet',
 'Mentoring',
 'APAC',
 'Framework',
 'Infrastructure',
 'Digital',
 'Surface',
 'SME',
 'Console',
 'Customer',
 'Intelligence',
 'Project',
 'Codes',
 'Ownership',
 'Reporting',
 'Engineers',
 'Displacement',
 'Coaching',
 'IP',
 'Unreal',
 'Git',
 'Facilitation',
 'Cisco',
 'Puppet',
 'Forecasting',
 'Liaison',
 'Capital',
 'Confluence',
 'TestNG',
 'Modeling',
 'REST',
 'Java',
 'Commission',
 'Enterprise',
 'English',
 'Azure',
 'Design',
 'Selenium',
 'Communications',
 'Tamil',
 'WIP',
 'EPANET',
 'Rigging',
 'Unix',
 'SAP']


df5 = pd.DataFrame(0, index=np.arange(len(l)), columns=s)
for i in range(len(l)):
    for x in l[i]:
        df5[x][i] = 1
frequent_itemsets = apriori(df5, min_support=0.080000000000000001, use_colnames=True) #0.080000000000000001
rules = association_rules(frequent_itemsets, metric='lift', min_threshold=1)
# rules.head()
def searchFilter(searchKey):
    results = []
    for i in range(len(rules['antecedents'])):
            if searchKey ==  list(rules['antecedents'][i])[0]:
                    results.extend(list(rules['consequents'][i]))
    results = set(results)
    return list(results)