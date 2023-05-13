"""
This file contains the base class for the load classes.
"""
import abc
from abc import ABC
from typing import Union

import numpy as np

from GHEtool.VariableClasses.BaseClass import BaseClass


class _LoadData(BaseClass, ABC):
    """
    This class contains information w.r.t. load data for the borefield sizing.
    """
    __slots__ = 'hourly_resolution', 'simulation_period', '_peak_heating_duration', '_peak_cooling_duration', 'tm'

    UPM: float = 730.  # number of hours per month
    DEFAULT_LENGTH_PEAK: int = 6  # hours

    def __init__(self, hourly_resolution: bool, simulation_period: int = 20):
        """

        Parameters
        ----------
        hourly_resolution : bool
            True if the load class uses an hourly resolution
        simulation_period : int
            Length of the simulation period in years
        """
        self.hourly_resolution: bool = hourly_resolution
        self.simulation_period: int = simulation_period
        self._peak_cooling_duration: int = _LoadData.DEFAULT_LENGTH_PEAK
        self._peak_heating_duration: int = _LoadData.DEFAULT_LENGTH_PEAK
        self.tm: int = _LoadData.UPM * 3600  # time in a month in seconds

    @abc.abstractmethod
    def _check_input(self, input: Union[np.ndarray, list, tuple]) -> bool:
        """
        This function checks whether the input is valid or not.

        Parameters
        ----------
        input : np.ndarray, list, tuple
            Thermal load input

        Returns
        -------
        bool
            True if the input is correct for the load class
        """

    @abc.abstractmethod
    def peak_heating(self) -> np.ndarray:
        """
        This function returns the peak heating load in kW/month.

        Returns
        -------
        peak heating : np.ndarray
        """

    @abc.abstractmethod
    def peak_cooling(self) -> np.ndarray:
        """
        This function returns the peak cooling load in kW/month.

        Returns
        -------
        peak cooling : np.ndarray
        """

    @abc.abstractmethod
    def baseload_heating(self) -> np.ndarray:
        """
        This function returns the baseload heating in kWh/month.

        Returns
        -------
        baseload heating : np.ndarray
        """

    @property
    def baseload_heating_power(self) -> np.ndarray:
        """
        This function returns the baseload heating in kW avg/month.

        Returns
        -------
        baseload heating : np.ndarray
        """
        return self.baseload_heating / _LoadData.UPM

    @abc.abstractmethod
    def baseload_cooling(self) -> np.ndarray:
        """
        This function returns the baseload cooling in kWh/month.

        Returns
        -------
        baseload cooling : np.ndarray
        """

    @property
    def baseload_cooling_power(self) -> np.ndarray:
        """
        This function returns the baseload cooling in kW avg/month.

        Returns
        -------
        baseload cooling : np.ndarray
        """
        return self.baseload_cooling / _LoadData.UPM

    def baseload_heating_simulation_period(self, sim_period: int) -> np.ndarray:
        """
        This function returns the baseload heating in kWh/month for a whole simulation period.

        Parameters
        ----------
        sim_period : int
            Length of the simulation period in years

        Returns
        -------
        baseload heating : np.ndarray
            baseload heating for the whole simulation period
        """
        return np.tile(self.baseload_heating, sim_period)

    @property
    def baseload_cooling_simulation_period(self) -> np.ndarray:
        """
        This function returns the baseload cooling in kWh/month for a whole simulation period.

        Returns
        -------
        baseload cooling : np.ndarray
            baseload cooling for the whole simulation period
        """
        return np.tile(self.baseload_cooling, self.simulation_period)

    @property
    def peak_heating_simulation_period(self) -> np.ndarray:
        """
        This function returns the peak heating in kW/month for a whole simulation period.

        Returns
        -------
        peak heating : np.ndarray
            peak heating for the whole simulation period
        """
        return np.tile(self.peak_heating, self.simulation_period)

    @property
    def peak_cooling_simulation_period(self) -> np.ndarray:
        """
        This function returns the peak cooling in kW/month for a whole simulation period.

        Returns
        -------
        peak cooling : np.ndarray
            peak cooling for the whole simulation period
        """
        return np.tile(self.peak_cooling, self.simulation_period)

    @property
    def baseload_heating_power_simulation_period(self) -> np.ndarray:
        """
        This function returns the avergae heating power in kW avg/month for a whole simulation period.

        Returns
        -------
        average heating power : np.ndarray
            average heating power for the whole simulation period
        """
        return np.tile(self.baseload_heating_power, self.simulation_period)

    @property
    def baseload_cooling_power_simulation_period(self) -> np.ndarray:
        """
        This function returns the average cooling power in kW avg/month for a whole simulation period.

        Returns
        -------
        average cooling power : np.ndarray
            average cooling for the whole simulation period
        """
        return np.tile(self.baseload_cooling_power, self.simulation_period)

    @property
    def imbalance(self) -> float:
        """
        This function calculates the ground imbalance.
        A positive imbalance means that the field is injection dominated, i.e. it heats up every year.

        Returns
        -------
        imbalance : float
        """
        return np.sum(self.baseload_cooling - self.baseload_heating)

    @property
    def monthly_average_load(self) -> np.ndarray:
        """
        This function calculates the average monthly load in kW.

        Returns
        -------
        monthly average load : np.ndarray
        """
        return self.baseload_cooling_power - self.baseload_heating_power

    @property
    def monthy_average_load_simulation_period(self) -> np.ndarray:
        """
        This function calculates the average monthly load in kW for the whole simulation period.

        Returns
        -------
        monthly average load : np.ndarray
        """
        return np.tile(self.monthly_average_load, self.simulation_period)
    @property
    def peak_heating_duration(self) -> float:
        """
        Length of the peak in heating.

        Returns
        -------
        Length peak in heating [s]
        """
        return self._peak_heating_duration

    @peak_heating_duration.setter
    def peak_heating_duration(self, duration: float) -> None:
        """
        This function sets the duration of the peak in heating.

        Parameters
        ----------
        duration : float
            Duration of the peak in hours

        Returns
        -------
        None
        """
        self._peak_heating_duration = duration * 3600

    @property
    def peak_cooling_duration(self) -> float:
        """
        Duration of the peak in cooling.

        Returns
        -------
        Duration of the peak in cooling [s]
        """
        return self._peak_cooling_duration

    @peak_cooling_duration.setter
    def peak_cooling_duration(self, duration: float) -> None:
        """
        This function sets the duration of the peak in cooling.

        Parameters
        ----------
        duration : float
            Duration of the peak in hours

        Returns
        -------
        None
        """
        self._peak_cooling_duration = duration * 3600
    @property
    def peak_duration(self) -> None:
        """
        Dummy object to set the length peak for both heating and cooling.

        Returns
        -------
        None
        """

    @peak_duration.setter
    def peak_duration(self, duration: float) -> None:
        """
        This sets the duration of both the heating and cooling peak.

        Parameters
        ----------
        duration : float
            Duration in hours

        Returns
        -------
        None
        """
        self.peak_heating_duration = duration
        self.peak_cooling_duration = duration

    @property
    def ty(self) -> float:
        """
        Simulation period in seconds.

        Returns
        -------
        Simulation period in seconds
        """
        return self.simulation_period * 8760 * 3600

    @property
    def time_L3(self) -> np.ndarray:
        """
        Time for L3 sizing, i.e. an array with monthly the cumulative seconds that have passed.
        [744, 1416 ...] * 3600

        Returns
        -------
        Times for the L3 sizing : np.ndarray
        """
        hours_per_month = np.array([744, 672, 744, 720, 744, 720, 744, 744, 720, 744, 720, 744])
        return np.cumsum(np.tile(hours_per_month, self.simulation_period) * 3600)

    @property
    def time_L4(self) -> np.ndarray:
        """
        Times for the L4 sizing, i.e. an array with hourly the cumulative seconds that have passed.
        [1, 2, 3, 4 ...] * 3600

        Returns
        -------
        Times for the L4 sizing : np.ndarray
        """
        # set the time constant for the L4 sizing
        time_L4 = 3600 * np.arange(1, 8760 * self.simulation_period + 1, dtype=np.float16)
        if np.isinf(time_L4).any():
            # 16 bit is not enough, go to 32
            time_L4 = 3600 * np.arange(1, 8760 * self.simulation_period + 1, dtype=np.float32)
        return time_L4

    def _calculate_last_year_params(self, HC: bool) -> tuple:
        """
        This function calculates the parameters for the sizing based on the last year of operation.
        This is needed for the L2 sizing.

        Parameters
        ----------
        HC : bool
            True if the borefield is limited by extraction load

        Returns
        -------
        th, qh, qm, qa : float
            Peak length [s], peak load [W], corresponding monthly load [W], yearly imbalance [W]
        """

        # convert imbalance to Watt
        qa = self.imbalance / 8760. * 1000

        if HC:
            # limited by extraction load

            # set length peak
            th = 3600. * self.peak_heating_duration

            # Select month with the highest peak load and take both the peak and average load from that month
            if np.max(self.peak_heating) != np.average(self.peak_heating):
                month_index = np.where(self.peak_heating == np.max(self.peak_heating))[0, 0]
            else:
                # if the peak is constant in all months, then the maximum of the baseload month is chosen
                month_index = np.where(self.baseload_heating_power == np.max(self.baseload_heating_power))[0, 0]
            qm = self.monthly_average_load[month_index] * 1000.
            qh = np.max(self.peak_heating) * 1000.

            # correct signs
            qm = -qm
            qa = -qa

        else:
            # limited by injection load

            # set length peak
            th = 3600. * self.peak_cooling_duration

            # Select month with the highest peak load and take both the peak and average load from that month
            if np.max(self.peak_cooling) != np.average(self.peak_cooling):
                month_index = np.where(self.peak_cooling == np.max(self.peak_cooling))[0, 0]
            else:
                # if the peak is constant in all months, then the maximum of the baseload month is chosen
                month_index = np.where(self.baseload_cooling_power == np.max(self.baseload_cooling_power))[0, 0]
            qm = self.monthly_average_load[month_index] * 1000.
            qh = np.max(self.peak_cooling) * 1000.

        return th, qh, qm, qa

    def _calculate_first_year_params(self, HC: bool) -> tuple:
        """
        This function calculates the parameters for the sizing based on the first year of operation.
        This is needed for the L2 sizing.

        Parameters
        ----------
        HC : bool
            True if the borefield is limited by extraction load

        Returns
        -------
        th, tpm, tcm, qh, qpm, qcm : float
            Peak duration [s], cumulative time passed at the start of the month [s],
            cumulative time passed at the end of the month [s], peak load [W],
            average cumulative load of the past months [W avg],
            average load of the current month [W avg]
        """

        if HC:
            # limited by extraction load

            # set peak length
            th = 3600. * self.peak_heating_duration

            # Select month with the highest peak load and take both the peak and average load from that month
            if np.max(self.peak_heating) != np.average(self.peak_heating):
                month_index = np.where(self.peak_heating == np.max(self.peak_heating))[0, 0]
            else:
                # if the peak is constant in all months, then the maximum of the baseload month is chosen
                month_index = np.where(self.baseload_heating_power == np.max(self.baseload_heating_power))[0, 0]

            qh = np.max(self.peak_heating) * 1000.

            qm = self.monthly_average_load[month_index] * 1000.

            if month_index < 1:
                qpm = 0
            else:
                qpm = np.sum(self.monthly_average_load[:month_index]) * 1000 / (month_index + 1)

            qm = -qm
        else:
            # limited by injection

            # set peak length
            th = 3600. * self.length_peak_cooling

            # Select month with the highest peak load and take both the peak and average load from that month
            # Select month with the highest peak load and take both the peak and average load from that month
            if np.max(self.peak_cooling) != np.average(self.peak_cooling):
                month_index = np.where(self.peak_cooling == np.max(self.peak_cooling))[0, 0]
            else:
                # if the peak is constant in all months, then the maximum of the baseload month is chosen
                month_index = np.where(self.baseload_cooling_power == np.max(self.baseload_cooling_power))[0, 0]

            qh = np.max(self.peak_cooling) * 1000.

            qm = self.monthly_average_load[month_index] * 1000.
            if month_index < 1:
                qpm = 0
            else:
                qpm = np.sum(self.monthly_average_load[:month_index]) * 1000 / (month_index + 1)

        tcm = self.time_L3[month_index]
        tpm = self.time_L3[month_index - 1] if month_index > 0 else 0

        return month_index