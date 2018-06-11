# Smart_Mutation_Operator_for_Python


Based on a paper
D.B.Brown, M.Vaughn, B.Liblit and T.Reps
The care and feeding of wild-caught mutants
ESEC/FSE 2017 Proceedings of the 2017 11th Joint Meeting on Foundations of Software Engineering
https://dl.acm.org/citation.cfm?id=3106280

usage : bin/genMut \<source dir>
\<source dir> need to be absolute path.
It check all .py files in \<source dir> recursively, and generate mutants for each of them.
ex) ./genMut ~/models/research/object_detection/
