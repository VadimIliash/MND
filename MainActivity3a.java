package com.example.mndlab3;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import java.util.Random;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void genetic(View view) {
        TextView textView = findViewById(R.id.textView7);
        EditText editText = findViewById(R.id.inputa);
        EditText editText1 = findViewById(R.id.inputb);
        EditText editText2 = findViewById(R.id.inputc);
        EditText editText3 = findViewById(R.id.inputd);
        EditText editText4 = findViewById(R.id.inputy);
        double a = Double.parseDouble(editText.getText().toString());
        double b = Double.parseDouble(editText1.getText().toString());
        double c = Double.parseDouble(editText2.getText().toString());
        double d = Double.parseDouble(editText3.getText().toString());
        double y = Double.parseDouble(editText4.getText().toString());
        Random random = new Random();
        boolean Succesful = false;
        double[][] population = new double[4][4];
        for (int i = 0; i < population.length; i++) {
            for (int j = 0; j < population[i].length; j++) {
                population[i][j] = (int) (1 + Math.random() * (y / 2));
            }
        }
        while (!Succesful) {
            double delta[] = new double[4];
            double roulette_parameter = 0;
            double chance_of_parenthood[] = new double[4];
            for (int i = 0; i < 4; i++) {
                delta[i] = Math.abs(y - (a * population[i][0] + b * population[i][1] + c * population[i][2] + d * population[i][3]));
                roulette_parameter += 1 / delta[i];
                if (delta[i] == 0) {
                    Succesful = true;
                    textView.setText("Знайдені корені рівняння:\nX1 = " + population[i][0] + "\nX2 = " + population[i][1] + "\nX3 = " + population[i][2] + "\nX4 = " + population[i][3]);
                }
            }
            if (Succesful) {
                break;
            }
            //шанси кожного члена популяції стати батьком
            chance_of_parenthood[0] = 1 / delta[0] / roulette_parameter;
            for (int i = 1; i < 4; i++) {
                chance_of_parenthood[i] = chance_of_parenthood[i - 1] + 1 / delta[i] / roulette_parameter;
            }
            double chance1 = random.nextDouble();
            double chance2 = random.nextDouble();
            double chance3 = random.nextDouble();
            double chance4 = random.nextDouble();
            double[] father1 = new double[4];
            double[] father2 = new double[4];
            double[] father3 = new double[4];
            double[] father4 = new double[4];
            //знаходження 1 та 2 батьків
            for (int i = 0; i < 4; i++) {
                if (chance1 < chance_of_parenthood[i]) {
                    father1 = population[i];
                    for (int j = 0; j < 4; j++) {
                        if (chance2 < chance_of_parenthood[j]) {

                            father2 = population[j];
                            break;
                        }
                    }
                    break;
                }
            }
            //знаходження 3 та 4 батьків
            for (int i = 0; i < 4; i++) {
                if (chance3 < chance_of_parenthood[i]) {
                    father3 = population[i];
                    for (int j = 0; j < 4; j++) {
                        if (chance4 < chance_of_parenthood[j]) {
                            father4 = population[j];
                            break;
                        }
                    }
                    break;
                }
            }
            //кросовер 1 та 2 батьків
            int index1 = random.nextInt(3);
            for (int i = 0; i <= index1; i++) {
                double k = father1[i];
                father1[i] = father2[i];
                father2[i] = k;
            }
            //кросовер 3 і 4 батьків
            int index2 = random.nextInt(3);
            for (int i = 0; i <= index2; i++) {
                double k = father3[i];
                father3[i] = father4[i];
                father4[i] = k;
            }
            //нова популяція
            population = new double[][]{father1, father2, father3, father4};

            double chance_of_mutation = random.nextDouble();
            //шанс мутації 20%
            if (chance_of_mutation < 0.2) {
                int mutation = random.nextInt(2);
                if (mutation == 0)
                    population[random.nextInt(4)][random.nextInt(4)] += 1;
                else population[random.nextInt(4)][random.nextInt(4)] -= 1;
            }
        }

    }
}