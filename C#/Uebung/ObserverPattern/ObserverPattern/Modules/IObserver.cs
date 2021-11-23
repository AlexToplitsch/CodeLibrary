using ObserverPattern.Modules;
using System;
using System.Collections.Generic;
using System.Text;

namespace ObserverPattern
{
    interface IObserver
    {
        void Update(WeatherStation ws);
        void Register(WeatherStation ws);
        void Unregister(WeatherStation ws);

    }
}
