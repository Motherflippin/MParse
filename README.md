#MParse

Quick and dirty mathematical parser, in Unicode Plain Text

##Command Syntax

`python3 MParse.py FileName.mp`

Will output the mathematical representation of the contents of FileName.mp


##Input Examples
`int _a dt = _v + C` will produce  `∫𝐀 dt = 𝐕 + C`

##Substitutions
_x -> 𝐗 
Bold, mainly for Vectors
int -> ∫
integral -> ∫
phi -> ϕ
theta -> θ 
rho -> ρ
omega -> ω 
