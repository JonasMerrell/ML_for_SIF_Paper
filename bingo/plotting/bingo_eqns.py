
class RN_data_funs:
    def Mu1(X_0, X_1, X_2=0, X_3=0):
        from numpy import sqrt, cos, sin
        M = (33622907.281902 - (33622908.186748 - (sqrt(X_0))))*((sqrt(X_0) - (-0.055040))*(0.480859) - ((2.129986)*(X_1))) - (-1.083060)
        
        ### TRIAL 2 ###
        M = ((-4.862855 - (X_0) - (-14.496016 + X_1) - (7.994456))*(((-4.862855 - (X_0))*(-4.862855 - (X_0) - (-14.496016 + X_1)) + 48.333960)*(X_1) - (-0.091848)))*(0.251563) + 1.055752
        #M = (-0.092176 + X_1)*((-2.404498 + X_0)*(X_0) + 0.484722) - (1905.566261) + 1906.231764 - ((-1.084407)*(sqrt(X_1)))
        return M
    
    def gu1(X_0, X_1, X_3, X_2):
        from numpy import sqrt, cos, sin
        g = (((sin(X_2) - (1.055261))*(X_1))*(-0.000110))*(4741.340369) + (0.114983)*(X_0) + 0.89453125
        #g =-53602933519417.929688 + (-0.054486 + ((0.896710)*(sin(X_2 + 3722.785157)) - (-0.984231))*(X_0))*(X_1 + -0.213224) - (-53602933519418.929688)
        
        ### TRIAL 2 ###
        g = cos((2.530161 + (((X_1)*(X_1))*(0.590023) + 0.437161)*(sin(X_2)) - ((X_1)*(X_1)))*(1.088869)) - (-2.000031)
        g = sin((-113.797854 + 114.873353)*((X_1 - (sin(X_2) + -0.055521))*(X_1) + -1.194459) + (0.140811)*(X_0)) + 1.983730
        return g
    
    def Mo1(X_0, X_1, X_2=0, X_3=0):
        from numpy import sqrt, cos, sin
        X_0 = 1/X_0
        M = sqrt(sqrt(X_0)) - (0.145056)
        return M
    
    def go1(X_0, X_1, X_3, X_2):
        from numpy import sqrt, cos, sin
        g = 1 + (0.1+0.35*((X_0**(-1)))*(X_1)**2)*(1-(sin(X_2)))**2
        return g


# RN Eqn

class RN_eqn_funs:
    def Mu1(X_0, X_1, X_2=0, X_3=0):
        from numpy import sqrt, cos, sin
        # sqrt3 = np.emath.sqrt
        # def sqrt(x):
        #     return abs(sqrt3(x))
        M = (((13.804167)*(X_0 - (3.565979)))*(sqrt(X_0)) + 36.977445)*((0.031819)*((X_1)*(X_1 - (-1.319777))) - (0.001833)) + 1.051169
        M = (sqrt(X_0)*(13.804167*X_0 - 49.225369634493) + 36.977445)*(0.031819*X_1*(X_1 + 1.319777) - 0.001833) + 1.051169
        
        ### TRIAL 2 ###
        #M = ((-0.124278 + 1.057496 + (1.405610 - (sqrt(X_0)))*((1.405610 - (sqrt(X_0)))*(X_1)))*(0.730550))*((1.405610 - (sqrt(X_0)))*((1.405610 - (sqrt(X_0)))*(X_1))) + 86.239802 - (43.129421) + -42.079126
        M = (((1.180636)*(sqrt(X_0)) + -1.438596)*(-0.217433 - (X_1)))*(((1.180636)*(sqrt(X_0)) + -1.438596)*(-0.217433 - (X_1))) + 62.414228 - (20.460517) - (20.229128) + -20.673957
        #M = ((-0.480718)*((2.798314)*(sqrt(0.202493 - (X_0))) + -2.634924))*(X_1 + -0.103196) - (4.054467) + 5.101003
        #M = 1.357489 + ((1.357489 - (sqrt(X_0)))*((1.357489 - (sqrt(X_0)))*(X_1)))*(1.228277) - (-38.163851) - (19.314149) + -19.210837
        #M = 1.34698*X_1*(1 - 0.711434893035764*sqrt(X_0))**2 + 1.03125499999999
        return M
    
    def gu1(X_0, X_1, X_3, X_2):
        from numpy import sqrt, cos, sin
        g = 0.9993 + (0.4085*X_1 + 0.2309)**2 * (1.0128 - sin(X_2))**2
        #g = 1 + (0.1 + 0.35*(X_1)**2)*(1-sin(X_2))**2
        
        ### TRIAL 2 ###
        g = (X_1 + 0.645087)*((X_1 + 0.645087)*(0.14846353627*sin(X_2) - 0.297424128459432)*sin(X_2) + 0.347009) + 0.803747
        return g
    
    def Mo1(X_0, X_1, X_2=0, X_3=0):
        from numpy import sqrt, cos, sin
        X_0 = 1/X_0
        M = ((X_0)*(0.274624) - (59882531.611787) + 59882531.514921)*((-0.352740 + X_0)*(X_1 + -1.793803 + -0.352740 + X_0) - (-3.116885)) - (-0.604788)
        
        ### TRIAL 2 ###
        M = sqrt(X_0)*((X_1 - 0.079181)*(0.746112*X_0*(sqrt(X_0) - 0.993416) + 0.119041) + 1.058784) - 0.0281910000012431
        ### STACK SIZE 30 ###
        M = (0.10565*(X_1 + 0.360041)*(X_0**2*(0.720527*X_1 - 0.352391021998) + 0.105133) - 0.2631525974)*((X_0 - (X_1 + 0.360041)*(-0.720527*X_0**2*(X_1 - 0.489074) - 0.105133) - 2.490796)*(-X_0**2 + (X_1 + 0.360041)*(-0.720527*X_0**2*(X_1 - 0.489074) - 0.105133) - 4.581786) - 16.295681) - 1.036403
        return M
    
    def go1(X_0, X_1, X_3, X_2):
        from numpy import sqrt, cos, sin
        g = 1 + (0.1+0.35*((X_0**(-1)))*(X_1)**2)*(1-(sin(X_2)))**2
        X_0 = 1/X_0
        #g = 0.999991 - (((8833227.041394 + (sin(X_2))*(1.999006) - (-1261496.774534) - ((sin(X_2))*(sin(X_2))) + -10094724.815343)*(X_1 + 0.222239))*(0.232156))
        
        ### TRIAL 2 ###
        g =  ((((-0.973016)*(sin(X_2)) - (-0.973278))*(-0.608237))*(((-0.973016)*(sin(X_2)) - (-0.973278))*(-0.608237)))*((X_0)*((X_1)*(X_1)) + 0.425402 + -0.140293) - (-0.999990)
        g = 0.35*(X_0*X_1**2 + 0.285109)*(sin(X_2) - 1)**2 + 1
        return g

# F3d data

class F3d_data_funs:
    def Mu1(X_0, X_1, X_2=0, X_3=0):
        from numpy import sqrt, cos, sin
        sqrt3 = np.emath.sqrt
        def sqrt(x):
            return abs(sqrt3(x))
        # orginial equation
        #M = 1.0052643174132263 - ((X_1)*((X_0 + -5.897146261824969)*(X_0) - ((-8.41374265030078)*(sqrt(X_0)) + 3.65713751815375)))
        
        M = (((sqrt(-0.341410 + sqrt(X_0)))*((-1.957341 + sqrt(-0.341410 + sqrt(X_0)))*(-0.139728)) - (0.132972))*(0.108615 - (X_1)))*(20.159387) + 1.051741
        #M = 1.05174 - 5.5135 *(sqrt(sqrt(X_0) - 0.34141) - 0.510897 *sqrt(X_0) - 0.311769) *(X_1 - 0.108615)
        
        
        ### TRIAL 2 ###
        #M = (-660.396388 + (-89.045028 - (-90.064271) - (X_0))*((0.008540 - (X_1))*(-89.045028 - (-90.064271) - (X_0)) + 0.106868))*(-1.517551) + -1001.092859
        M = (1.114310)*(-63.472139 + (1.122792 - (sqrt(X_0 + -0.208461)))*((1.122792 - (sqrt(X_0 + -0.208461)))*(-0.111355 + X_1))) - (-36.533956 + -35.246715)
        return M
    
    def gu1(X_0, X_1, X_2, X_3):
        X_2 = X_3
        from numpy import sqrt, cos, sin
        #g = 1 + (0.1 + 0.35*(X_1)**2)*(1-sin(X_2))**2
        g = (1.0263496149498648 + sin(6373.023412385456 + 11071.131423790328 + -11350.186594670391 - (6373.023412385456 - (sin(X_3)))))*(X_1) + cos(11071.131423790328)
        g = -(-1.0263496149499*X_1 + X_1*sin(279.05517088006 - sin(X_3)) - 0.9873999518025)
        
        
        ### TRIAL 2 ###
        g = (((1.015248 - (sin(X_2)))*(-0.061607))*(-7.069833) + -5.222969 + (X_1)*(X_1) + 2.775947 - (-2.266952))*(((1.015248 - (sin(X_2)))*(-0.061607))*(-7.069833)) + sqrt(1.015248)
        
        return g
    
    def Mo1(X_0, X_1, X_2=0, X_3=0):
        from numpy import sqrt, cos, sin
        # original equation
        # sqrt3 = np.emath.sqrt
        # def sqrt(x):
        #     return abs(sqrt3(x))
        X_0 = 1/X_0
        #M = (X_0)*(0.2965415493436768) - (-0.02115042312837423) + (sqrt(X_1))*((sqrt(X_0))*(0.2502798692342405 + 0.2502798692342405) - (0.3628181028391626)) + (sqrt(sqrt(X_0)))*(0.6637021883924064)
        M = (X_0 + -4.120056 + (X_1)*(-2.311179))*(((sqrt(X_1) + -3.330640)*(X_0))*(0.066869) + -217034054.103521 - (-217034054.146461)) - (-0.504788)
        
        ### TRIAL 2 ###
        #M = sqrt(((-0.764500 + X_0)*(-0.852586 - (X_1)) + 0.186688)*((X_1)*(-0.764500) - (-2.200765)) + -1.997414 - (1.365838)) - (0.819053)
        M = 0.790029 - ((-0.585648 + X_0)*((0.156573)*(54911.261124 + X_0 - (28145.860335) + -26770.085597 + (-1.440581)*(X_1))))
        return M
    
    def go1(X_0, X_1, X_2, X_3):
        from numpy import sqrt, cos, sin
        # opriginal equation used RN g
        X_2 = X_3
        X_0 = 1/X_0
        g = 1 + (0.1+0.35*((X_0))*(X_1)**2)*(1-(sin(X_3)))**2
        #g = 1.313275 + (cos(((0.770511)*(X_1) - ((0.336310)*(0.336310)))*(X_0) + -1.674651 - (sin(X_2)) + -0.577035))*(0.313262)
        
        ### TRAIL 2 ###
        g = (118.696317 + sin((cos(X_1) + 1.306766 + sin(X_2))*(0.476230)) - (119.687454))*(-0.505565 - (X_0)) + 1.008365
        #g = (sin(sin(X_2) + ((X_1)*(X_0 + 0.257186))*(-0.564576) + 0.758759))*(-54.537231 - (-54.224772)) + 1.312375
        return g
