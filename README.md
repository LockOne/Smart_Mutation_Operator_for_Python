# Smart_Mutation_Operator_for_Python


Based on a paper
D.B.Brown, M.Vaughn, B.Liblit and T.Reps
The care and feeding of wild-caught mutants
ESEC/FSE 2017 Proceedings of the 2017 11th Joint Meeting on Foundations of Software Engineering
https://dl.acm.org/citation.cfm?id=3106280

usage : __bin/genMut /some/directory/of/project/__  
The path need to be absolute path.  
It check all .py files in /some/directory/ recursively, and generate mutants for each of them.
ex) ./genMut __~/models/research/object_detection/__

usage : bin/checkMut /some/directory/of/mutants/  
/some/mutants/ need to be absolute path.  
It checks mutants in mutants/ and count number of .py files with syntax error.
