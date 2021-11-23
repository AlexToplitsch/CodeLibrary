namespace SuperaAdventure
{
    partial class SuperAdventure
    {
        /// <summary>
        /// Erforderliche Designervariable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Verwendete Ressourcen bereinigen.
        /// </summary>
        /// <param name="disposing">True, wenn verwaltete Ressourcen gelöscht werden sollen; andernfalls False.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Vom Windows Form-Designer generierter Code

        /// <summary>
        /// Erforderliche Methode für die Designerunterstützung.
        /// Der Inhalt der Methode darf nicht mit dem Code-Editor geändert werden.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(SuperAdventure));
            this.btnNorth = new System.Windows.Forms.Button();
            this.btnSouth = new System.Windows.Forms.Button();
            this.btnWest = new System.Windows.Forms.Button();
            this.btnEast = new System.Windows.Forms.Button();
            this.pictBox_Street = new System.Windows.Forms.PictureBox();
            this.backgroundWorker1 = new System.ComponentModel.BackgroundWorker();
            this.TxtBox_Info = new System.Windows.Forms.RichTextBox();
            this.Btn_Fight = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictBox_Street)).BeginInit();
            this.SuspendLayout();
            // 
            // btnNorth
            // 
            this.btnNorth.Location = new System.Drawing.Point(553, 437);
            this.btnNorth.Name = "btnNorth";
            this.btnNorth.Size = new System.Drawing.Size(75, 30);
            this.btnNorth.TabIndex = 0;
            this.btnNorth.Text = "Norden";
            this.btnNorth.UseVisualStyleBackColor = true;
            this.btnNorth.Click += new System.EventHandler(this.btnNorth_Click_1);
            // 
            // btnSouth
            // 
            this.btnSouth.Location = new System.Drawing.Point(553, 557);
            this.btnSouth.Name = "btnSouth";
            this.btnSouth.Size = new System.Drawing.Size(75, 30);
            this.btnSouth.TabIndex = 1;
            this.btnSouth.Text = "Süden";
            this.btnSouth.UseVisualStyleBackColor = true;
            this.btnSouth.Click += new System.EventHandler(this.btnSouth_Click);
            // 
            // btnWest
            // 
            this.btnWest.Location = new System.Drawing.Point(478, 498);
            this.btnWest.Name = "btnWest";
            this.btnWest.Size = new System.Drawing.Size(75, 30);
            this.btnWest.TabIndex = 2;
            this.btnWest.Text = "Westen";
            this.btnWest.UseVisualStyleBackColor = true;
            this.btnWest.Visible = false;
            this.btnWest.Click += new System.EventHandler(this.btnWest_Click);
            // 
            // btnEast
            // 
            this.btnEast.Location = new System.Drawing.Point(630, 503);
            this.btnEast.Name = "btnEast";
            this.btnEast.Size = new System.Drawing.Size(75, 30);
            this.btnEast.TabIndex = 3;
            this.btnEast.Text = "Osten";
            this.btnEast.UseVisualStyleBackColor = true;
            this.btnEast.Click += new System.EventHandler(this.btnEast_Click);
            // 
            // pictBox_Street
            // 
            this.pictBox_Street.Image = ((System.Drawing.Image)(resources.GetObject("pictBox_Street.Image")));
            this.pictBox_Street.Location = new System.Drawing.Point(13, 13);
            this.pictBox_Street.Name = "pictBox_Street";
            this.pictBox_Street.Size = new System.Drawing.Size(692, 331);
            this.pictBox_Street.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictBox_Street.TabIndex = 4;
            this.pictBox_Street.TabStop = false;
            this.pictBox_Street.Click += new System.EventHandler(this.pictBox_Street_Click);
            // 
            // TxtBox_Info
            // 
            this.TxtBox_Info.Location = new System.Drawing.Point(13, 367);
            this.TxtBox_Info.Name = "TxtBox_Info";
            this.TxtBox_Info.ReadOnly = true;
            this.TxtBox_Info.Size = new System.Drawing.Size(450, 268);
            this.TxtBox_Info.TabIndex = 5;
            this.TxtBox_Info.Text = resources.GetString("TxtBox_Info.Text");
            this.TxtBox_Info.ZoomFactor = 1.4F;
            this.TxtBox_Info.TextChanged += new System.EventHandler(this.TxtBox_Info_TextChanged);
            // 
            // Btn_Fight
            // 
            this.Btn_Fight.Location = new System.Drawing.Point(630, 367);
            this.Btn_Fight.Name = "Btn_Fight";
            this.Btn_Fight.Size = new System.Drawing.Size(75, 32);
            this.Btn_Fight.TabIndex = 6;
            this.Btn_Fight.Text = "Fight";
            this.Btn_Fight.UseVisualStyleBackColor = true;
            this.Btn_Fight.Visible = false;
            this.Btn_Fight.Click += new System.EventHandler(this.Btn_Fight_Click);
            // 
            // SuperAdventure
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ControlLightLight;
            this.ClientSize = new System.Drawing.Size(717, 643);
            this.Controls.Add(this.Btn_Fight);
            this.Controls.Add(this.TxtBox_Info);
            this.Controls.Add(this.pictBox_Street);
            this.Controls.Add(this.btnEast);
            this.Controls.Add(this.btnWest);
            this.Controls.Add(this.btnSouth);
            this.Controls.Add(this.btnNorth);
            this.Name = "SuperAdventure";
            this.Text = "Tourguide";
            this.Load += new System.EventHandler(this.SuperAdventure_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictBox_Street)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnNorth;
        private System.Windows.Forms.Button btnSouth;
        private System.Windows.Forms.Button btnWest;
        private System.Windows.Forms.Button btnEast;
        private System.Windows.Forms.PictureBox pictBox_Street;
        private System.ComponentModel.BackgroundWorker backgroundWorker1;
        private System.Windows.Forms.RichTextBox TxtBox_Info;
        private System.Windows.Forms.Button Btn_Fight;
    }
}

