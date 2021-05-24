package com.example.mndlab1a;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.Gravity;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void factorization(View view) {
        long starttime = System.nanoTime();
        EditText editText = findViewById(R.id.input_number);
        TextView textView = findViewById(R.id.textView3);
        int num = Integer.parseInt(editText.getText().toString());
        int a = (int) Math.ceil(Math.sqrt(num));
        if ((num & 1) == 0) {
            textView.setText("Число є парним:\n " + num + " = " + num / 2 + " * " + 2);
        } else {
            while (!isPerfectSquare(a * a - num)) {
                a += 1;
            }
            int b = (int) Math.sqrt(a * a - num);
            long endTime = System.nanoTime();
            if ((endTime - starttime) > Math.pow(10, 9)) {
                Toast toast = Toast.makeText(this, "Помилка виконання програми!", Toast.LENGTH_LONG);
                toast.setGravity(Gravity.CENTER, 0,0);
                toast.show();
            } else
                textView.setText("Результат факторизації:\n" + num + " = " + (a - b) + " * " + (a + b));

        }
    }

    public boolean isPerfectSquare(int n) {
        int sqr = (int) Math.sqrt(n);
        return sqr * sqr == n;
    }
}