package com.example.mndlab2;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import com.google.android.material.chip.Chip;
import com.google.android.material.chip.ChipGroup;

public class MainActivity extends AppCompatActivity {

    static int min(long a[]) {
        int min = 0;
        for (int i = 1; i < a.length; i++) {
            if (a[min] > a[i]) min = i;
        }
        return min;
    }
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

    }

    public void click(View view) {
        TextView tw = findViewById(R.id.textView4);
        double Speed_Of_Training[] = {0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09};
        ChipGroup cg2 = findViewById(R.id.cg2);
        Chip c2 = findViewById(cg2.getCheckedChipId());
        double Time_Limit = Double.parseDouble(c2.getText().toString());
        ChipGroup cg3 = findViewById(R.id.cg3);
        Chip c3 = findViewById(cg3.getCheckedChipId());
        double Number_Of_Iterations = Double.parseDouble(c3.getText().toString());
        tw.setText("");
        long time[]=new long[9];
        for (int i = 0; i < 9; i++) {
            int Current_Iteration = 0;
            int P = 4;
            int Succesful = 0;
            double W1 = 0;
            double W2 = 0;
            int[][] points = {{0, 6}, {1, 5}, {3, 3}, {2, 4}};
            long start = System.nanoTime();

            while ((((System.nanoTime() - start) / Math.pow(10, 9)) < Time_Limit) &&
                    (Current_Iteration < Number_Of_Iterations) && (Succesful < 4)) {
                int Point_Index = Current_Iteration % 4;
                double y = W1 * points[Point_Index][0] + W2 * points[Point_Index][1];

                if (((y > P) && (Point_Index < 2)) || ((y < P) && (Point_Index > 1))) {
                    Succesful++;
                    Current_Iteration++;
                    continue;
                }
                double Delta = P - y;
                W1 = W1 + Delta * points[Point_Index][0] * Speed_Of_Training[i];
                W2 = W2 + Delta * points[Point_Index][1] * Speed_Of_Training[i];
                Current_Iteration++;
                Succesful = 0;
            }
            time[i]=System.nanoTime() - start;
            tw.setText(tw.getText()+"\nW1=" + W1 + " W2=" + W2 + "\nЧас виконання="+ time[i] + " нс, сігма="+Speed_Of_Training[i])
            ;
        }
        tw.setText(tw.getText()+"\nНайкращий час виконання з сігма="+Speed_Of_Training[min(time)]);
    }
}