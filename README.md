# chemeq

High school chemistry teacher contacted me asking if I know of any tools to easily convert organic chemical equations to their corresponding diagrams. Couldn't find something... so I built it.

Instructions:
Open the link below –
https://salty-wildwood-57739.herokuapp.com/hello

Type the equation in words. The equations need to follow this format:

compound name -> compound name + compound name 

Using the `->` is important. It is minus sign (-) followed by a greater than sign (>). Using equal will not work.

Examples:
1. benzoyl chloride + H2 -> benzaldehyde (you can mix and match formulae like H2 with compounds names like benzaldehyde)
2. toluene + cl2 -> benzal chloride
3. Benzoic acid -> m- Nitrobenzyl alcohol


Notes:
1. Currently this generates images, which you can then copy and paste onto word. I can change this to write things in letters if you like.
2. Currently, it only supports single equations at a time. Cannot write benzoyl chloride -> benzaldehyde -> benzene in one go. I can add this too if you need.
3. Only supports chemical formula right now. Can possibly add diagrams for organic chemistry (like display benzene ring with CH3 instead of C7H8 when you type toluene)... But I will need to make a list of compounds for which we want image vs. chemical formula
4. I know it is a little slow right now, but what I can do is add maybe 5 or 10 text boxes, then you can input all of the equations that you want together, press submit and let it take a couple of seconds to generate all equations at the same time!
