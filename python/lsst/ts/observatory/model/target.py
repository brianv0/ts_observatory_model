import math
import numpy
import json


__all__ = ["Target"]


class Target(object):
    """Class for gathering information for a sky target.
    """

    def __init__(self, targetid=0, fieldid=0, band_filter="",
                 ra_rad=0.0, dec_rad=0.0, ang_rad=0.0,
                 num_exp=0, exp_times=[]):
        """Initialize the class.

        Parameters
        ----------
        targetid : int
            A unique identifier for the given target.
        fieldid : int
            The ID of the associated OpSim field for the target.
        band_filter : str
            The single character name of the associated band filter.
        ra_rad : float
            The right ascension (radians) of the target.
        dec_rad : float
            The declination (radians) of the target.
        ang_rad : float
            The sky angle (radians) of the target.
        num_exp : int
            The number of requested exposures for the target.
        exp_times : list[float]
            The set of exposure times for the target. Needs to length
            of num_exp.
        """
        self.targetid = targetid
        self.fieldid = fieldid
        self.filter = band_filter
        self.ra_rad = ra_rad
        self.dec_rad = dec_rad
        self.ang_rad = ang_rad
        self.num_exp = num_exp
        self.exp_times = list(exp_times)
        self._exp_time = None  # total exposure time

        # conditions
        self.time = 0.0
        self.airmass = 0.0
        self.sky_brightness = 0.0
        self.cloud = 0.0
        self.seeing = 0.0

        # computed at driver
        self.alt_rad = 0.0
        self.az_rad = 0.0
        self.rot_rad = 0.0
        self.telalt_rad = 0.0
        self.telaz_rad = 0.0
        self.telrot_rad = 0.0
        self.slewtime = 0.0

        self.note = ''

    def __str__(self):
        """str: The string representation of the instance."""
        return ("targetid=%d field=%d filter=%s exp_times=%s ra=%.3f "
                "dec=%.3f ang=%.3f alt=%.3f az=%.3f rot=%.3f "
                "telalt=%.3f telaz=%.3f telrot=%.3f "
                "time=%.1f airmass=%.3f brightness=%.3f "
                "cloud=%.2f seeing=%.2f "
                "slewtime=%.3f note=%s" %
                (self.targetid, self.fieldid, self.filter,
                 str(self.exp_times),
                 self.ra, self.dec, self.ang,
                 self.alt, self.az, self.rot,
                 self.telalt, self.telaz, self.telrot,
                 self.time, self.airmass, self.sky_brightness,
                 self.cloud, self.seeing,
                 self.slewtime,self.note))

    @property
    def alt(self):
        """float: The altitude (degrees) of the target."""
        return math.degrees(self.alt_rad)

    @alt.setter
    def alt(self, alt):
        """
        Set altitude given in degrees

        Parameters
        ----------
         alt: float (degrees)
        """
        self.alt_rad = math.radians(alt)

    @property
    def ang(self):
        """float: The sky angle (degrees) of the target."""
        return math.degrees(self.ang_rad)

    @ang.setter
    def ang(self, ang):
        """
        Set camera rotation angle given in degrees

        Parameters
        ----------
         ang: float (degrees)
        """
        self.ang_rad = math.radians(ang)

    @property
    def az(self):
        """float: The azimuth (degrees) of the target."""
        return math.degrees(self.az_rad)

    @az.setter
    def az(self, az):
        """
        Set camera rotation angle given in degrees

        Parameters
        ----------
         az: float (degrees)
        """
        self.az_rad = math.radians(az)

    @property
    def dec(self):
        """float: The declination (degrees) of the target."""
        return math.degrees(self.dec_rad)

    @dec.setter
    def dec(self, dec):
        """
        Set declination given in degrees

        Parameters
        ----------
         dec: float (degrees)
        """
        self.dec_rad = math.radians(dec)

    @property
    def ra(self):
        """float: The right ascension (degrees) of the target."""
        return math.degrees(self.ra_rad)

    @ra.setter
    def ra(self, ra):
        """
        Set right ascension given in degrees

        Parameters
        ----------
         ra: float (degrees)
        """
        self.ra_rad = math.radians(ra)

    @property
    def rot(self):
        """float: The rotator angle (degrees) of the target."""
        return math.degrees(self.rot_rad)

    @rot.setter
    def rot(self, rot):
        """
        Set camera rotation angle given in degrees

        Parameters
        ----------
         rot: float (degrees)
        """
        self.rot_rad = math.radians(rot)

    @property
    def telalt(self):
        """float: The telescope altitude (degrees) for the target."""
        return math.degrees(self.telalt_rad)

    @telalt.setter
    def telalt(self, telalt):
        """
        Set camera rotation angle given in degrees

        Parameters
        ----------
         telalt: float (degrees)
        """
        self.telalt_rad = math.radians(telalt)

    @property
    def telaz(self):
        """float: The telescope azimuth (degrees) for the target."""
        return math.degrees(self.telaz_rad)

    @telaz.setter
    def telaz(self, telaz):
        """
        Set camera rotation angle given in degrees

        Parameters
        ----------
         telaz: float (degrees)
        """
        self.telaz_rad = math.radians(telaz)

    @property
    def telrot(self):
        """float: The telescope rotator angle (degrees) for the target."""
        return math.degrees(self.telrot_rad)

    @telrot.setter
    def telrot(self, telrot):
        """
        Set camera rotation angle given in degrees

        Parameters
        ----------
         telrot: float (degrees)
        """
        self.telrot_rad = math.radians(telrot)

    @property
    def exp_time(self):
        """

        Returns
        -------
        exp_time: float: The total exposure time in seconds.
        """
        if self._exp_time is None:
            return sum(self.exp_times)
        else:
            return self._exp_time

    @exp_time.setter
    def exp_time(self, exp_time):
        """

        Parameters
        ----------
        exp_time: float: The total exposure time in seconds.

        Returns
        -------
        None
        """
        self._exp_time = exp_time

    def copy_driver_state(self, target):
        """Copy driver state from another target.

        Parameters
        ----------
        target : :class:`.Target`
            An instance of a target from which to get the driver state
            information.
        """
        self.alt_rad = target.alt_rad
        self.az_rad = target.az_rad
        self.rot_rad = target.rot_rad
        self.telalt_rad = target.telalt_rad
        self.telaz_rad = target.telaz_rad
        self.telrot_rad = target.telrot_rad
        self.ang_rad = target.ang_rad

    def get_copy(self):
        """:class:`.Target`: Get copy of the instance."""
        newtarget = Target()
        newtarget.targetid = self.targetid
        newtarget.fieldid = self.fieldid
        newtarget.filter = self.filter
        newtarget.ra_rad = self.ra_rad
        newtarget.dec_rad = self.dec_rad
        newtarget.ang_rad = self.ang_rad
        newtarget.num_exp = self.num_exp
        newtarget.exp_times = list(self.exp_times)

        newtarget.time = self.time
        newtarget.airmass = self.airmass
        newtarget.sky_brightness = self.sky_brightness
        newtarget.cloud = self.cloud
        newtarget.seeing = self.seeing

        newtarget.alt_rad = self.alt_rad
        newtarget.az_rad = self.az_rad
        newtarget.rot_rad = self.rot_rad
        newtarget.telalt_rad = self.telalt_rad
        newtarget.telaz_rad = self.telaz_rad
        newtarget.telrot_rad = self.telrot_rad
        newtarget.slewtime = self.slewtime

        newtarget.note = self.note

        return newtarget

    def to_json(self):
        """
        Returns a json serialization of variables in this object
        """
        return json.dumps(vars(self))

    def from_json(self, jsonstr):
        """
        alternate __init__ method that takes a json representation as the only argument
        """
        mandatory_fields = ["targetid", "fieldid", "filter", "ra_rad", "dec_rad",
                            "ang_rad", "num_exp", "exp_times"]

        jsondict = json.loads(jsonstr)
        for f in mandatory_fields:
            if f not in jsondict.keys():
                raise KeyError("json blob passed to Target()'s json constructor "
                               "is missing required attribute: " + f)


        for k in jsondict:
            setattr(self, k, jsondict[k])

    @classmethod
    def from_topic(cls, topic):
        """Alternate initializer.

        Parameters
        ----------
        topic : SALPY_scheduler.targetC
            The target topic instance.

        Returns
        -------
        :class:`.Target`
        """
        return cls(topic.targetId, -1, topic.filter, math.radians(topic.ra),
                   math.radians(topic.decl), math.radians(topic.skyAngle), topic.numExposures,
                   topic.exposureTimes)
