using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace GUI_1
{
    public partial class mainFrm : Form
    {
        public mainFrm()
        {
            InitializeComponent();
            
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void mainFrm_Load(object sender, EventArgs e)
        {
            tbResult.ReadOnly = true;
        }

        private void black(object sender, EventArgs e)
        {

        }

        private void Add_Click(object sender, EventArgs e)
        {
            string num1_str = tbNum1.Text;
            string num2_str = tbNum2.Text;

            double num1 = double.Parse(num1_str);
            double num2 = double.Parse(num2_str);

            double sum = num1 + num2;

            tbResult.Text = sum.ToString();
        }

        private void Mul_Click(object sender, EventArgs e)
        {
            string num1_str = tbNum1.Text;
            string num2_str = tbNum2.Text;

            double num1 = double.Parse(num1_str);
            double num2 = double.Parse(num2_str);

            double sum = num1 * num2;

            tbResult.Text = sum.ToString();
        }

        private void Sub_Click(object sender, EventArgs e)
        {
            string num1_str = tbNum1.Text;
            string num2_str = tbNum2.Text;

            double num1 = double.Parse(num1_str);
            double num2 = double.Parse(num2_str);

            double sum = num1 - num2;

            tbResult.Text = sum.ToString();
        }

        private void Div_Click(object sender, EventArgs e)
        {
            string num1_str = tbNum1.Text;
            string num2_str = tbNum2.Text;

            double num1 = double.Parse(num1_str);
            double num2 = double.Parse(num2_str);

            if (num2 == 0)
            {
                tbResult.Text = "Error: Div by 0";
                lbError.Text = "Cannot divide by zero.";
                MessageBox.Show("Cannot divide by zero.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            else
            {

                double sum = num1 / num2;

                tbResult.Text = sum.ToString();
            }
         }

        private void bt_Execute_Click(object sender, EventArgs e)
        {
            double num1 = double.Parse(tbNum1.Text);
            double num2 = double.Parse(tbNum2.Text);
            double result = 0;

            if (rb_Add.Checked)
            {
                result = num1 + num2;
            }
            else if (rb_Sub.Checked)
            {
                result = num1 - num2;
            }
            else if (rb_Mul.Checked)
            {
                result = num1 * num2;
            }
            else if (rb_Div.Checked)
            {
                result = num1 / num2;
            }

            tbResult.Text = result.ToString();
            

        }

        private void bt_Clear_Click(object sender, EventArgs e)
        {
            tbNum1.Text = "";
            tbNum2.Text = "";
            tbResult.Text = "";
            lbError.Text = "";
        }
    }
}
