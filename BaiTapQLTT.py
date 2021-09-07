import turtle
shapeInput = input('Hình bạn muốn vẽ là hình tròn hay hình vuông :')
if shapeInput == 'Hình tròn' or shapeInput == 'Hình vuông':
	colorInput  = input('Bạn muốn chọn màu vàng, mà đỏ hày màu xanh? :')

	if colorInput == 'yellow' or colorInput =='red' or colorInput == 'blue':
		pen = turtle.Screen()
		pen = bgcolor("black")
		pen = title("Your shape")

		displayShape = turtle.Turtle()
		displayShape.shape(shapeInput)
		displayShape.color(colorInput)

		turtle.done()
	else:
		print("Xin lỗi. Tôi không có màu này. (")

else:
	print("Xin lỗi. Tôi không có hình vẽ này. (")	