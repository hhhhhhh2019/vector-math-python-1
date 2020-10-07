from math import acos


# МАТРИЦЫ
class mat2:
	def __init__(self, a, b):
		self.mat = [
			[a.x, a.y],
			[b.x, b.y]]

class mat3:
	def __init__(self, a, b, c):
		self.mat = [
			[a.x, a.y, a.z],
			[b.x, b.y, b.z],
			[c.x, c.y, c.z]]

class mat4:
	def __init__(self, a, b, c, d):
		self.mat = [
			[a.x, a.y, a.z, a.w],
			[b.x, b.y, b.z, b.w],
			[c.x, c.y, c.z, c.w],
			[d.x, d.y, d.z, d.w]]


# ВЕКТОРЫ
class vec2:
	x, y = 0, 0
	
	def __init__(self, x: float = 0, y: float = x):
		self.x, self.y = x, y
	
	# сложение
	def __add__(self, a):
		if isinstance(a, vec2):
			return vec2(self.x + a.x, self.y + a.y)
		
		elif isinstance(a, tuple) and len(a) == 2:
			return vec2(self.x + a[0], self.y + a[1])
		
		else:
			if isinstance(a, str):
				raise TypeError("unsupported operand type(s) for +: 'vec2' and 'str'")
			if isinstance(a, int):
				raise TypeError("unsupported operand type(s) for +: 'vec2' and 'int'")
			if isinstance(a, float):
				raise TypeError("unsupported operand type(s) for +: 'vec2' and 'float'")
			if isinstance(a, mat2):
				raise TypeError("unsupported operand type(s) for +: 'vec2' and 'mat2'")
			if isinstance(a, mat3):
				raise TypeError("unsupported operand type(s) for +: 'vec2' and 'mat3'")
			if isinstance(a, mat4):
				raise TypeError("unsupported operand type(s) for +: 'vec2' and 'mat4'")
			if isinstance(a, vec3):
				raise TypeError("unsupported operand type(s) for +: 'vec2' and 'vec3'")
			if isinstance(a, vec4):
				raise TypeError("unsupported operand type(s) for +: 'vec2' and 'vec4'")
	
	# вычитание
	def __sub__(self, a):
		if isinstance(a, vec2):
			return vec2(self.x - a.x, self.y - a.y)
		
		elif isinstance(a, tuple) and len(a) == 2:
			return vec2(self.x - a[0], self.y - a[1])
		
		else:
			if isinstance(a, str):
				raise TypeError("unsupported operand type(s) for -: 'vec2' and 'str'")
			if isinstance(a, int):
				raise TypeError("unsupported operand type(s) for -: 'vec2' and 'int'")
			if isinstance(a, float):
				raise TypeError("unsupported operand type(s) for -: 'vec2' and 'float'")
			if isinstance(a, mat2):
				raise TypeError("unsupported operand type(s) for -: 'vec2' and 'mat2'")
			if isinstance(a, mat3):
				raise TypeError("unsupported operand type(s) for -: 'vec2' and 'mat3'")
			if isinstance(a, mat4):
				raise TypeError("unsupported operand type(s) for -: 'vec2' and 'mat4'")
			if isinstance(a, vec3):
				raise TypeError("unsupported operand type(s) for -: 'vec2' and 'vec3'")
			if isinstance(a, vec4):
				raise TypeError("unsupported operand type(s) for -: 'vec2' and 'vec4'")
	
	# умножение
	def __mul__(self, a):
		if isinstance(a, vec2):
			return vec2(self.x * a.x, self.y * a.y)
		
		elif isinstance(a, tuple) and len(a) == 2:
			return vec2(self.x * a[0], self.y * a[1])
		
		elif isinstance(a, mat2):
			return vec2(
				a.mat[0][0] * self.x + a.mat[0][1] * self.y,
				a.mat[1][0] * self.x + a.mat[1][1] * self.y
			)
		
		else:
			if isinstance(a, str):
				raise TypeError("unsupported operand type(s) for *: 'vec2' and 'str'")
			if isinstance(a, int):
				raise TypeError("unsupported operand type(s) for *: 'vec2' and 'int'")
			if isinstance(a, float):
				raise TypeError("unsupported operand type(s) for *: 'vec2' and 'float'")
			if isinstance(a, mat3):
				raise TypeError("unsupported operand type(s) for *: 'vec2' and 'mat3'")
			if isinstance(a, mat4):
				raise TypeError("unsupported operand type(s) for *: 'vec2' and 'mat4'")
			if isinstance(a, vec3):
				raise TypeError("unsupported operand type(s) for *: 'vec2' and 'vec3'")
			if isinstance(a, vec4):
				raise TypeError("unsupported operand type(s) for *: 'vec2' and 'vec4'")
	
	# деление
	def __truediv__(self, a):
		if isinstance(a, vec2):
			return vec2(self.x / a.x, self.y / a.y)
		
		elif isinstance(a, tuple) and len(a) == 2:
			return vec2(self.x / a[0], self.y / a[1])
		
		else:
			if isinstance(a, str):
				raise TypeError("unsupported operand type(s) for /: 'vec2' and 'str'")
			if isinstance(a, int):
				raise TypeError("unsupported operand type(s) for /: 'vec2' and 'int'")
			if isinstance(a, float):
				raise TypeError("unsupported operand type(s) for /: 'vec2' and 'float'")
			if isinstance(a, mat2):
				raise TypeError("unsupported operand type(s) for /: 'vec2' and 'mat2'")
			if isinstance(a, mat3):
				raise TypeError("unsupported operand type(s) for /: 'vec2' and 'mat3'")
			if isinstance(a, mat4):
				raise TypeError("unsupported operand type(s) for /: 'vec2' and 'mat4'")
			if isinstance(a, vec3):
				raise TypeError("unsupported operand type(s) for /: 'vec2' and 'vec3'")
			if isinstance(a, vec4):
				raise TypeError("unsupported operand type(s) for /: 'vec2' and 'vec4'")
	
	def __abs__(self):
		return self.size
	
	def __len__(self):
		return self.size
	
	def __iter__(self):
		for i in self.xy:
			yield i
	
	# свойства xy, yx
	# xy
	@property
	def xy(self):
		return self.x, self.y
	
	@xy.setter
	def xy(self, a):
		if isinstance(a, vec2):
			self.x, self.y = a.xy
		
		elif isinstance(a, tuple):
			self.x, self.y = a
	
	# yx
	@property
	def yx(self):
		return self.y, self.x
	
	@yx.setter
	def yx(self, a):
		if isinstance(a, vec2):
			self.y, self.x = a.yx
		
		elif isinstance(a, tuple):
			self.y, self.x = a
	
	# длинна
	@property
	def size(self):
		return (self.x ** 2 + self.y ** 2) ** 0.5
	
	# угол
	@property
	def angle(self):
		return acos(dot(self, vec2(1, 0)) / self.size)


class vec3:
	x, y, z = 0, 0, 0
	
	def __init__(self, x: float = 0, y: float = x, z: float = x):
		self.x, self.y = x, y
	
	# сложение
	def __add__(self, a):
		if isinstance(a, vec3):
			return vec3(self.x + a.x, self.y + a.y, self.z + a.z)
		
		elif isinstance(a, tuple) and len(a) == 3:
			return vec3(self.x + a[0], self.y + a[1], self.z + a[2])
		
		else:
			if isinstance(a, str):
				raise TypeError("unsupported operand type(s) for +: 'vec3' and 'str'")
			if isinstance(a, int):
				raise TypeError("unsupported operand type(s) for +: 'vec3' and 'int'")
			if isinstance(a, float):
				raise TypeError("unsupported operand type(s) for +: 'vec3' and 'float'")
			if isinstance(a, mat2):
				raise TypeError("unsupported operand type(s) for +: 'vec3' and 'mat2'")
			if isinstance(a, mat3):
				raise TypeError("unsupported operand type(s) for +: 'vec3' and 'mat3'")
			if isinstance(a, mat4):
				raise TypeError("unsupported operand type(s) for +: 'vec3' and 'mat4'")
			if isinstance(a, vec3):
				raise TypeError("unsupported operand type(s) for +: 'vec3' and 'vec2'")
			if isinstance(a, vec4):
				raise TypeError("unsupported operand type(s) for +: 'vec3' and 'vec4'")
	
	# вычитание
	def __sub__(self, a):
		if isinstance(a, vec3):
			return vec3(self.x - a.x, self.y - a.y, self.z - a.z)
		
		elif isinstance(a, tuple) and len(a) == 3:
			return vec3(self.x - a[0], self.y - a[1], self.z - a[2])
		
		else:
			if isinstance(a, str):
				raise TypeError("unsupported operand type(s) for -: 'vec3' and 'str'")
			if isinstance(a, int):
				raise TypeError("unsupported operand type(s) for -: 'vec3' and 'int'")
			if isinstance(a, float):
				raise TypeError("unsupported operand type(s) for -: 'vec3' and 'float'")
			if isinstance(a, mat2):
				raise TypeError("unsupported operand type(s) for -: 'vec3' and 'mat2'")
			if isinstance(a, mat3):
				raise TypeError("unsupported operand type(s) for -: 'vec3' and 'mat3'")
			if isinstance(a, mat4):
				raise TypeError("unsupported operand type(s) for -: 'vec3' and 'mat4'")
			if isinstance(a, vec3):
				raise TypeError("unsupported operand type(s) for -: 'vec3' and 'vec2'")
			if isinstance(a, vec4):
				raise TypeError("unsupported operand type(s) for -: 'vec3' and 'vec4'")
	
	# умножение
	def __mul__(self, a):
		if isinstance(a, vec3):
			return vec3(self.x * a.x, self.y * a.y, self.z * a.z)
		
		elif isinstance(a, tuple) and len(a) == 3:
			return vec3(self.x * a[0], self.y * a[1], self.z * a[2])
		
		elif isinstance(a, mat3):
			return vec3(
				a.mat[0][0] * self.x + a.mat[0][1] * self.y + a.mat[0][2] * self.z,
				a.mat[1][0] * self.x + a.mat[1][1] * self.y + a.mat[1][2] * self.z,
				a.mat[2][0] * self.x + a.mat[2][1] * self.y + a.mat[2][2] * self.z
			)
		
		else:
			if isinstance(a, str):
				raise TypeError("unsupported operand type(s) for *: 'vec3' and 'str'")
			if isinstance(a, int):
				raise TypeError("unsupported operand type(s) for *: 'vec3' and 'int'")
			if isinstance(a, float):
				raise TypeError("unsupported operand type(s) for *: 'vec3' and 'float'")
			if isinstance(a, mat2):
				raise TypeError("unsupported operand type(s) for *: 'vec3' and 'mat2'")
			if isinstance(a, mat4):
				raise TypeError("unsupported operand type(s) for *: 'vec3' and 'mat4'")
			if isinstance(a, vec2):
				raise TypeError("unsupported operand type(s) for *: 'vec3' and 'vec2'")
			if isinstance(a, vec4):
				raise TypeError("unsupported operand type(s) for *: 'vec3'' and 'vec4'")
	
	# деление
	def __truediv__(self, a):
		if isinstance(a, vec3):
			return vec3(self.x / a.x, self.y / a.y, self.z / a.z)
		
		elif isinstance(a, tuple) and len(a) == 3:
			return vec4(self.x / a[0], self.y / a[1], self.z / a[2])
		
		else:
			if isinstance(a, str):
				raise TypeError("unsupported operand type(s) for /: 'vec3' and 'str'")
			if isinstance(a, int):
				raise TypeError("unsupported operand type(s) for /: 'vec3' and 'int'")
			if isinstance(a, float):
				raise TypeError("unsupported operand type(s) for /: 'vec3' and 'float'")
			if isinstance(a, mat2):
				raise TypeError("unsupported operand type(s) for /: 'vec3' and 'mat2'")
			if isinstance(a, mat3):
				raise TypeError("unsupported operand type(s) for /: 'vec3' and 'mat3'")
			if isinstance(a, mat4):
				raise TypeError("unsupported operand type(s) for /: 'vec3' and 'mat4'")
			if isinstance(a, vec2):
				raise TypeError("unsupported operand type(s) for /: 'vec3' and 'vec2'")
			if isinstance(a, vec4):
				raise TypeError("unsupported operand type(s) for /: 'vec3(' and 'vec4'")
	
	def __abs__(self):
		return self.size
	
	def __len__(self):
		return self.size
	
	def __iter__(self):
		for i in self.xy:
			yield i
	
	# свойства xy, yx, xz, zx, yz, zy, xyz, zyx, yzx, xzy
	# xy
	@property
	def xy(self):
		return self.x, self.y
	
	@xy.setter
	def xy(self, a):
		if isinstance(a, vec2):
			self.x, self.y = a.xy
		
		elif isinstance(a, tuple):
			self.x, self.y = a
	
	# yx
	@property
	def yx(self):
		return self.y, self.x
	
	@yx.setter
	def yx(self, a):
		if isinstance(a, vec2):
			self.y, self.x = a.yx
		
		elif isinstance(a, tuple):
			self.y, self.x = a
	
	# xz
	@property
	def xz(self):
		return self.x, self.z
	
	@xz.setter
	def xz(self, a):
		if isinstance(a, vec2):
			self.x, self.z = a.xz
		
		elif isinstance(a, tuple):
			self.x, self.z = a
	
	# zx
	@property
	def zx(self):
		return self.z, self.x
	
	@xz.setter
	def zx(self, a):
		if isinstance(a, vec2):
			self.z, self.x = a.zx
		
		elif isinstance(a, tuple):
			self.z, self.x = a
	
	# yz
	@property
	def yz(self):
		return self.y, self.z
	
	@yz.setter
	def yz(self, a):
		if isinstance(a, vec2):
			self.y, self.z = a.yz
		
		elif isinstance(a, tuple):
			self.y, self.z = a
	
	# zy
	@property
	def zy(self):
		return self.z, self.y
	
	@xz.setter
	def xz(self, a):
		if isinstance(a, vec2):
			self.z, self.y = a.zy
		
		elif isinstance(a, tuple):
			self.z, self.y = a
	
	# xyz
	@property
	def xyz(self):
		return self.x, self.y, self.z
	
	@xyz.setter
	def xyz(self, a):
		if isinstance(a, vec3):
			self.x, self.y, self.z = a.xyz
		
		elif isinstance(a, tuple):
			self.x, self.y, self.z = a
	
	# xzy
	@property
	def xzy(self):
		return self.x, self.z, self.y
	
	@xzy.setter
	def xzy(self, a):
		if isinstance(a, vec3):
			self.x, self.z, self.y = a.xzy
		
		elif isinstance(a, tuple):
			self.x, self.z, self.y = a
	
	# длинна
	@property
	def size(self):
		return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5


class vec4:
	pass


# функции с векторами
def dot(a, b):
	v = a * b
	res = 0
	
	for i in v:
		res += i
	
	return res

def distance(a, b):
	return len(a - b)

def norm(a):
	return a / len(a)
