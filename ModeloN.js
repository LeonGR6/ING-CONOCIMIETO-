// Definición de la clase Perceptron
class Perceptron {
    constructor(w0, w1, w2, a) {
        this.w0 = w0;
        this.w1 = w1;
        this.w2 = w2;
        this.a = a;
        this.x0 = [1, 1, 1, 1];
        this.x1 = [1, 1, -1, -1];
        this.x2 = [1, -1, 1, -1];
        this.yd = [1, -1, -1, -1];
    }

    operacionY(index) {
        let y;
        if (index === 0) {
            y = this.x0[index] * this.w0 + this.x1[index] * this.w1 + this.x2[index] * this.w2;
        } else if (index === 1) {
            y = this.x0[index] * this.w0 + this.x1[index] * this.w1 + this.x2[index] * this.w2;
        } else if (index === 2) {
            y = this.x0[index] * this.w0 + this.x1[index] * this.w1 + this.x2[index] * this.w2;
        }
        return y >= 0 ? 1 : -1;
    }

    recalcularPesos(index) {
        let error = this.yd[index] - this.operacionY(index);
        this.w0 = this.w0 + this.a * error * this.x0[index];
        this.w1 = this.w1 + this.a * error * this.x1[index];
        this.w2 = this.w2 + this.a * error * this.x2[index];
        console.log("Calculando Pesos");
        console.log("Los nuevos pesos son");
        console.log("W0= " + this.w0);
        console.log("W1= " + this.w1);
        console.log("W2= " + this.w2);
    }

    mostrarPesos() {
        console.log(">>>");
        console.log("Los pesos Finales Fueron");
        console.log("W0= " + this.w0);
        console.log("W1= " + this.w1);
        console.log("W2= " + this.w2);
    }

    entrenar() {
        let todosCorrectos;
        do {
            todosCorrectos = true;
            for (let i = 0; i < this.x0.length; i++) {
                let error = this.yd[i] - this.operacionY(i);
                if (error !== 0) {
                    todosCorrectos = false;
                    this.recalcularPesos(i);
                }
                console.log(`x0: ${this.x0[i]}, x1: ${this.x1[i]}, x2: ${this.x2[i]}, yd: ${this.yd[i]}, Y: ${this.operacionY(i)}, error: ${error}`);
                
            }
        } while (!todosCorrectos);
        this.mostrarPesos();
    }
}

// Instanciamos y entrenamos el perceptrón
const perceptron = new Perceptron(0, 0, 0, 0.4);
perceptron.entrenar();
