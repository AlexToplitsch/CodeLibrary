using System;
using System.Collections.Generic;
using System.Text;

namespace ObserverPattern.Modules
{
    class WeatherStation : ISubject
    {
        public string Name { get; private set; }
        public string Time { get; set; }
        public float Temp { get; set; } = 0;
        public float Moisture { get; set; } = 0;
        private float LastTemp { get; set; } = 0;
        private float LastMoist { get; set; } = 0;
        private List<IObserver> Clients { get; set; } = new List<IObserver>();
        
        public WeatherStation(string name)
        {
            Name = name;
        }

        public void Run(bool run = true)
        {
            int i = 0;
            while (run == true)
            {
                Measure();
                System.Threading.Thread.Sleep(800);
                i++;
                if(i > 3)
                {
                    run = false;
                }
            }
        }

        public void Notify()
        {
            foreach (IObserver client in Clients)
            {
                client.Update(this);
            }
        }

        public void Register(IObserver observer)
        {
            Clients.Add(observer);
        }

        public void Unregister(IObserver observer)
        {
            try
            {
                Clients.Remove(observer);
            }
            catch
            {
                throw new Exception("Objekt kann nicht entfernt werden, da es nicht registriert ist.");
            }
        }

        private void CompareData()
        {
            if (Temp < LastTemp - 1 || Temp > LastTemp + 1)
            {
                Notify();
            }
            else if (Moisture < LastMoist - 5 || Moisture > LastMoist + 5)
            {
                Notify();
            }
        }

        private void Measure()
        {
            Random rnd = new Random();
            Temp = (float)(rnd.NextDouble() * 100 - 40);
            Moisture = (float)rnd.NextDouble() * 100;
            Time = Convert.ToString(DateTime.Now);
            CompareData();
        }
    }
}
