def bouncing_ball(h, bounce, window):
    # your code
    rebounds = -1
    if bounce > 0 and bounce < 1:
        if h > 0:
            while h > window:
                rebounds += 2
                h *= bounce
            return rebounds        
    
    return -1


print(bouncing_ball(2, 0.5, 1))
print(bouncing_ball(3, 0.66, 1.5))
print(bouncing_ball(30, 0.66, 1.5))
print(bouncing_ball(30, 0.75, 1.5))

# @test.it('Fixed Tests')
#     def tests():
#         testing(2, 0.5, 1, 1)
#         testing(3, 0.66, 1.5, 3)
#         testing(30, 0.66, 1.5, 15)
#         testing(30, 0.75, 1.5, 21)